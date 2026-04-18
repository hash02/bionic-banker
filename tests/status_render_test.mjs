// Headless DOM render smoke test for status.html.
// No Puppeteer needed — we parse the HTML, inject the JSON as a fake fetch,
// and evaluate the inline script against a fake document to confirm it runs
// without throwing and produces the expected DOM updates.
import fs from "node:fs";
import path from "node:path";

const ROOT = "/sessions/happy-adoring-galileo/mnt/hash 2026/bionic-banker";
const html = fs.readFileSync(path.join(ROOT, "status.html"), "utf8");
const json = JSON.parse(fs.readFileSync(path.join(ROOT, "dashboard-data/status.json"), "utf8"));

// 1) Parse inline <script> IIFE
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (!scriptMatch) { console.error("FAIL: no inline <script>"); process.exit(1); }
const scriptBody = scriptMatch[1];

// 2) Build a minimal DOM shim
const nodes = {};
function mkNode(id) {
  const n = {
    id, _text: "", _html: "", _class: "",
    insertedAfter: [], insertedBefore: [],
    set textContent(v) { this._text = String(v); },
    get textContent() { return this._text; },
    set innerHTML(v) { this._html = String(v); },
    get innerHTML() { return this._html; },
    set className(v) { this._class = String(v); },
    get className() { return this._class; },
    insertAdjacentHTML(pos, h) { (pos==="beforeend"?this.insertedAfter:this.insertedBefore).push(h); },
  };
  nodes[id] = n; return n;
}
const ids = [
  "ts","pnl","wr","trades","workers","hermes-note","aml","aml-body","site","site-body",
  "wukong","wukong-body","content","content-body","fires-body"
];
ids.forEach(mkNode);

const fakeDoc = {
  getElementById: id => nodes[id] || (mkNode(id)),
  querySelector: sel => { if (sel===".wrap") return { insertAdjacentHTML() {} }; return null; },
};
global.document = fakeDoc;
global.fetch = async () => ({ json: async () => json });
global.Date = Date;

// 3) Run the IIFE in global scope with shimmed document + fetch
globalThis.document = fakeDoc;
globalThis.fetch = global.fetch;
try {
  const { runInThisContext } = await import("node:vm");
  // The script body IS an IIFE; wrap the IIFE itself in an async function so we can await.
  await runInThisContext(`(async () => { ${scriptBody} })()`);
} catch (e) {
  console.error("FAIL: script threw", e.message);
  console.error(e.stack?.split("\n").slice(0,5).join("\n"));
  process.exit(1);
}
// Give the async IIFE a tick to finish its await fetch
await new Promise(r => setTimeout(r, 50));

// 4) Assert expected fields populated
const checks = [
  ["ts text set",       nodes["ts"]._text.length > 10],
  ["pnl shows -$",      nodes["pnl"]._text.includes("$") && nodes["pnl"]._text.includes("-")],
  ["pnl class red",     nodes["pnl"]._class.includes("red")],
  ["wr shows %",        nodes["wr"]._text.includes("%")],
  ["trades shows open", nodes["trades"]._text.includes("open")],
  ["workers rendered",  nodes["workers"]._html.includes("polymarket_bonds")],
  ["workers has grid",  nodes["workers"]._html.includes("grid_eth_usdc")],
  ["aml body filled",   nodes["aml-body"]._html.includes("17")],
  ["aml notes stale",   nodes["aml-body"]._html.includes("stale") || nodes["aml"].insertedAfter.some(h=>h.includes("stale"))],
  ["site shows 40",     nodes["site-body"]._html.includes("40")],
  ["wukong disk",       nodes["wukong-body"]._html.includes("48")],
  ["content warn pill", nodes["content-body"]._html.includes("warn")],
  ["fires rendered",    nodes["fires-body"]._html.includes("done") || nodes["fires-body"]._html.includes("pending")],
];
let pass = 0, fail = 0;
for (const [name, ok] of checks) {
  console.log(`${ok?"✓":"✗"} ${name}`);
  ok ? pass++ : fail++;
}
console.log(`\n${pass}/${checks.length} passed`);
if (fail) process.exit(1);
