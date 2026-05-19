const f="/dashboard-data/funds/portfolio_summary.json",v={fund_60_40_income:{title:"60/40 Income",sub:"Conservative. Yield-first."},fund_75_25_balanced:{title:"75/25 Balanced",sub:"Balanced. Mixed risk."},fund_90_10_growth:{title:"90/10 Growth",sub:"Aggressive. Momentum + sniper."}},l=e=>{if(e==null)return"—";const s=Math.abs(e),n=e<0?"-":"";return s>=1e3?n+"$"+Math.round(s).toLocaleString():n+"$"+s.toFixed(2)},u=e=>e==null?"—":(e>=0?"+":"")+"$"+e.toFixed(2),c=e=>e==null?"—":e<60?Math.round(e)+"m":(e/60).toFixed(1)+"h";function m(e){const s=e.aggregate||{};document.getElementById("agg-coverage").textContent=(s.coverage_pct||0).toFixed(1)+"%",document.getElementById("agg-exposure").textContent=l(s.exposure_usd);const n=document.getElementById("agg-pnl");n.textContent=u(s.pnl_usd),n.classList.toggle("accent",(s.pnl_usd||0)>0),document.getElementById("agg-funds").textContent=(s.funds_count||0)+" / "+(s.sleeves_funded||0)+"-"+(s.sleeves_total||0);const o=e.workers||{},t=Object.values(o).filter(d=>d.heartbeat_fresh).length;document.getElementById("agg-workers").textContent=t+" / "+Object.keys(o).length;const a=new Date(e.generated_iso),r=Math.round((Date.now()-a.getTime())/6e4);document.getElementById("sync-ts").textContent="synced "+(r<=1?"just now":r+"m ago")}function _(e){const s=document.getElementById("fund-grid");s.innerHTML="";const n=e.funds||{};Object.keys(v).forEach(o=>{const t=n[o];if(!t)return;const a=v[o],r=Object.entries(t.sleeves||{}).map(([g,i])=>`<div class="sleeve-row">
        <span><span class="sleeve-dot ${i.funded?"funded":""}"></span><span class="sleeve-name">${g}</span></span>
        <span class="sleeve-pos">${i.positions_total||0} pos · ${l(i.open_exposure_usd)}</span>
      </div>`).join(""),d=(t.pnl_usd||0)>0?"pos":(t.pnl_usd||0)<0?"neg":"";s.insertAdjacentHTML("beforeend",`
      <div class="fund-card">
        <div>
          <h3>${a.title}</h3>
          <div class="fund-sub">${a.sub}</div>
        </div>
        <div>
          <div class="coverage-bar"><div class="coverage-fill" style="width:${t.coverage_pct}%"></div></div>
          <div class="coverage-label">
            <span>Coverage</span>
            <strong>${t.sleeves_funded}/${t.sleeves_total} · ${t.coverage_pct.toFixed(1)}%</strong>
          </div>
        </div>
        <div class="fund-stats">
          <div>
            <div class="fund-stat-label">Exposure</div>
            <div class="fund-stat-val">${l(t.exposure_usd)}</div>
          </div>
          <div>
            <div class="fund-stat-label">Unrealized PnL</div>
            <div class="fund-stat-val ${d}">${u(t.pnl_usd)}</div>
          </div>
        </div>
        <div class="sleeve-list">${r}</div>
      </div>
    `)})}function k(e){const s=document.getElementById("worker-table");Array.from(s.querySelectorAll(".worker-row:not(.head), .loader")).forEach(o=>o.remove());const n=e.workers||{};Object.entries(n).forEach(([o,t])=>{const a=t.heartbeat_fresh,r=(t.strategy||"—").replace(/_/g," "),d=t.deployed_usd!==null&&t.deployed_usd!==void 0?l(t.deployed_usd):"—";s.insertAdjacentHTML("beforeend",`
      <div class="worker-row">
        <div class="worker-name">${o}</div>
        <div class="worker-meta">${r}</div>
        <div class="worker-col-hide-mobile"><span class="badge ${a?"ok":"stale"}">${a?"live":t.status||"stale"}</span></div>
        <div class="worker-col-hide-mobile worker-meta">#${t.cycle_count||0}</div>
        <div class="worker-col-hide-mobile worker-meta">${c(t.age_minutes)}</div>
        <div class="worker-col-hide-mobile worker-meta">${t.open_positions||0} · ${d}</div>
      </div>
    `)})}function h(e){const s=e.hermes||{},n=`
    <div class="kv-row"><span class="kv-key">Mode</span><span class="kv-val">${s.mode||"paper"}</span></div>
    <div class="kv-row"><span class="kv-key">Paper portfolio age</span><span class="kv-val">${c(s.paper_portfolio_age_min)}</span></div>
    <div class="kv-row"><span class="kv-key">Status age</span><span class="kv-val">${c(s.orchestrator_age_min)}</span></div>
    <div class="kv-row"><span class="kv-key">Total positions</span><span class="kv-val">${s.paper_portfolio_positions||0}</span></div>
    <div class="kv-row"><span class="kv-key">Currently open</span><span class="kv-val">${s.paper_portfolio_open||0}</span></div>
  `;document.getElementById("hermes-panel").innerHTML=n}async function p(){try{const e=await fetch(f,{cache:"no-store"});if(!e.ok)throw new Error("fetch failed "+e.status);const s=await e.json();m(s),_(s),k(s),h(s)}catch(e){document.getElementById("sync-ts").textContent="sync error — retry soon",console.error(e)}}p();setInterval(p,6e4);
