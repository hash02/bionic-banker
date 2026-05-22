# CloudCode Bionic Lab — Turn 002: /advisor/ Beta View

Generated: `2026-05-23T03:50:00Z`

Turn: CC-002 | Agent: CloudCode | Board: Bionic Lab
Previous: cloudcode-bionic-lab-turn-001 (turns 001-004 reviewed + turn 005 directed: Market Pulse + Agent Status)
This turn: Turn 006 directive — /advisor/ beta view

---

## North Star Connection

NORTH_STAR.md §3 Move #4: "Ship /advisor/ beta view — One public page rendering one pulse_event in human terms."

This is the deliverable. Not a dashboard. Not a chart. One page. One sentence. Current signal in plain English, grounded in real data.

"BTC is signaling UP with 62% confidence based on 3,162 observations. Accuracy last 100: 55%."

That is the product.

---

## Prerequisite Check

Turn 005 (Market Pulse + Agent Status) must be built and pushed before turn 006 runs. If you haven't done turn 005 yet, stop here and do that first. The routing is already wired — /advisor will just be a new route on the same SPA.

---

## Turn 006: /advisor/ Beta View

### What This Page Does

One sentence. Current BTC signal. Ground truth numbers. No sliders, no charts, no interactive elements.

Human reads it and immediately understands:
- What is the system predicting right now
- How confident it is
- How accurate it has been
- When this was last updated

Nothing else.

---

### Data Source

`public/dashboard-data/heartbeat.json` — already used in Signal Intelligence module. The /advisor view reads the same file. No new API calls.

Key fields to surface:
- `status.last_prediction.value.direction` → "up" or "down"
- `status.last_prediction.value.confidence` → 0-1 float
- `status.accuracy_last_100` → 0-1 float (percentage)
- `status.predictions_made` → integer
- `status.iso` → last update timestamp
- `status.last_prediction.value.sub_scores` → det, ml, llm (for sub-panel)

---

### Create `src/modules/Advisor/index.tsx`

Replace the placeholder with:

```tsx
import { useState, useEffect } from 'react'

interface HeartbeatSnapshot {
  generated_at: string
  status: {
    iso: string
    alive: boolean
    mode: string
    predictions_made: number
    accuracy_last_100: number
    last_prediction: {
      value: {
        direction: 'up' | 'down'
        confidence: number
        method: string
        sub_scores: {
          det: number
          ml: number
          llm: number
        }
      }
      price_now?: number
    }
  }
}

function pct(v: number): string {
  return `${(v * 100).toFixed(0)}%`
}

function confPct(v: number): string {
  return `${(v * 100).toFixed(1)}%`
}

function dirLabel(dir: 'up' | 'down'): string {
  return dir === 'up' ? 'UP' : 'DOWN'
}

function dirColor(dir: 'up' | 'down'): string {
  return dir === 'up' ? '#1fa068' : '#e44'
}

function formatTs(iso: string): string {
  try {
    const d = new Date(iso)
    return d.toLocaleString('en-CA', {
      month: 'short', day: 'numeric',
      hour: '2-digit', minute: '2-digit',
      timeZoneName: 'short',
    })
  } catch {
    return iso
  }
}

export default function Advisor() {
  const [hb, setHb] = useState<HeartbeatSnapshot | null>(null)
  const [error, setError] = useState(false)

  useEffect(() => {
    window.fetch('/dashboard-data/heartbeat.json')
      .then(r => { if (!r.ok) throw new Error(); return r.json() })
      .then((d: HeartbeatSnapshot) => setHb(d))
      .catch(() => setError(true))
  }, [])

  if (error) {
    return (
      <div style={{ fontFamily: 'monospace', color: '#888890', fontSize: '0.85rem' }}>
        Signal unavailable — heartbeat offline.
      </div>
    )
  }

  if (!hb) {
    return (
      <div style={{ fontFamily: 'monospace', color: '#888890', fontSize: '0.85rem' }}>
        Loading signal...
      </div>
    )
  }

  const s = hb.status
  const pred = s.last_prediction.value
  const dir = pred.direction
  const conf = pred.confidence
  const acc = s.accuracy_last_100
  const totalPreds = s.predictions_made

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem', maxWidth: '720px' }}>

      {/* Primary signal sentence */}
      <div style={{
        backgroundColor: '#0e0e12',
        border: `1px solid ${dirColor(dir)}33`,
        borderRadius: '0.75rem',
        padding: '2rem',
      }}>
        <div style={{
          fontFamily: 'monospace',
          fontSize: '0.6rem',
          textTransform: 'uppercase',
          letterSpacing: '0.12em',
          color: '#888890',
          marginBottom: '1rem',
        }}>
          Current Signal
        </div>

        <p style={{
          fontFamily: 'monospace',
          fontSize: '1.15rem',
          color: '#e4e4ec',
          lineHeight: 1.7,
          margin: 0,
        }}>
          BTC is signaling{' '}
          <strong style={{ color: dirColor(dir), fontSize: '1.25rem' }}>
            {dirLabel(dir)}
          </strong>
          {' '}with{' '}
          <strong style={{ color: '#e4e4ec' }}>{confPct(conf)}</strong>
          {' '}confidence based on{' '}
          <strong style={{ color: '#e4e4ec' }}>{totalPreds.toLocaleString()}</strong>
          {' '}observations.
          {' '}Accuracy last 100:{' '}
          <strong style={{ color: acc >= 0.55 ? '#1fa068' : '#888890' }}>
            {pct(acc)}
          </strong>
          .
        </p>

        <div style={{
          fontFamily: 'monospace',
          fontSize: '0.62rem',
          color: '#555560',
          marginTop: '1.25rem',
        }}>
          Last updated: {formatTs(s.iso)}
          {s.last_prediction.price_now && (
            <span> · BTC ${s.last_prediction.price_now.toLocaleString('en-US', { maximumFractionDigits: 0 })}</span>
          )}
        </div>
      </div>

      {/* Sub-scores panel */}
      <div style={{
        backgroundColor: '#0e0e12',
        border: '1px solid rgba(31, 160, 104, 0.1)',
        borderRadius: '0.75rem',
        padding: '1.25rem 1.5rem',
      }}>
        <div style={{
          fontFamily: 'monospace',
          fontSize: '0.6rem',
          textTransform: 'uppercase',
          letterSpacing: '0.12em',
          color: '#555560',
          marginBottom: '1rem',
        }}>
          Signal Breakdown
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '1rem' }}>
          {[
            { label: 'Deterministic', key: 'det', value: pred.sub_scores.det },
            { label: 'ML Ensemble', key: 'ml', value: pred.sub_scores.ml },
            { label: 'LLM Gate', key: 'llm', value: pred.sub_scores.llm },
          ].map(({ label, value }) => {
            const isPositive = value >= 0
            return (
              <div key={label} style={{ display: 'flex', flexDirection: 'column', gap: '0.25rem' }}>
                <span style={{ fontFamily: 'monospace', fontSize: '0.58rem', color: '#555560', textTransform: 'uppercase', letterSpacing: '0.08em' }}>
                  {label}
                </span>
                <strong style={{
                  fontFamily: 'monospace',
                  fontSize: '1.1rem',
                  color: isPositive ? '#1fa068' : '#e44444',
                  lineHeight: 1,
                }}>
                  {value >= 0 ? '+' : ''}{value.toFixed(3)}
                </strong>
              </div>
            )
          })}
        </div>
      </div>

      {/* Context */}
      <div style={{
        backgroundColor: '#0e0e12',
        border: '1px solid rgba(31, 160, 104, 0.08)',
        borderRadius: '0.75rem',
        padding: '1.25rem',
      }}>
        <div style={{
          fontFamily: 'monospace',
          fontSize: '0.6rem',
          textTransform: 'uppercase',
          letterSpacing: '0.12em',
          color: '#555560',
          marginBottom: '0.75rem',
        }}>
          What This Is
        </div>
        <p style={{ fontFamily: 'monospace', fontSize: '0.75rem', color: '#888890', lineHeight: 1.65, margin: 0 }}>
          This signal is generated by a live system running on a private server. It combines deterministic indicators (RSI, MACD, funding rate, open interest), a machine learning ensemble, and a language model gate. Each prediction is scored against actual BTC price movement 15 minutes later. The accuracy figure reflects real scored outcomes, not backtested projections. This is a research tool, not investment advice.
        </p>
      </div>

      <div style={{ fontFamily: 'monospace', fontSize: '0.62rem', color: '#444450', textAlign: 'right' }}>
        Bionic Banker · Research only · Not investment advice
      </div>
    </div>
  )
}
```

---

### Route Registration

Open `src/App.tsx`. The route for `/advisor` should already exist as a placeholder. Confirm the import and route are wired:

```tsx
import Advisor from './modules/Advisor'
// ...
<Route path="/advisor" element={<Layout title="Advisor"><Advisor /></Layout>} />
```

If the placeholder path is different, adjust to match your existing routing pattern.

---

### Nav Link

In the navigation component (wherever the sidebar/nav links are defined), add:

```tsx
{ path: '/advisor', label: 'Advisor' }
```

This makes the page reachable from the nav, not just direct URL.

---

## Codex Task for Turn 006

1. Create `src/modules/Advisor/index.tsx` — replace placeholder with code above
2. Wire the route in `src/App.tsx` (confirm `/advisor` path exists and imports Advisor module)
3. Add nav link for Advisor
4. Run `npm run build` — 0 TypeScript errors expected
5. Push to GitHub — Cloudflare auto-deploys
6. Verify: visit `/advisor` directly. Should show one sentence with direction, confidence, total predictions, accuracy. Sub-scores panel below. Context block below that.
7. Test with heartbeat.json: the file at `public/dashboard-data/heartbeat.json` must have real values. If heartbeat.json is the sample/placeholder, the page will show sample data — that is OK for the build. Real data flows when Wukong's heartbeat cron next runs.

Do NOT change Financial Planning, AML Monitor, Signal Intelligence, Market Pulse, or Agent Status in this turn.

---

## Definition of Done for Turn 006

The page passes this test: someone who has never heard of this project can read `/advisor`, understand what the system is predicting, why they should trust or distrust the number (accuracy baseline), and what the signal is built from — in under 30 seconds, without clicking anything.

One public page. One sentence. Real numbers. No fluff.

That is North Star Move #4. When this is live, write the handoff to turn 007 immediately.

---

## Turn 007 Preview

After /advisor is live: wire auto-refresh. The heartbeat.json updates every ~5-15 minutes on Wukong's cron. Add a `setInterval` in the Advisor component that re-fetches the JSON every 60 seconds. The signal timestamp updates. No page reload needed. The page becomes a live ticker.

Then: public URL. Not buried in the Bionic Banker app. A shareable link: `bionicbanker.tech/advisor` (if DNS is wired to the same Cloudflare app) or the Cloudflare Pages preview URL. HASH shares this with one person. That is the beta test.

---

## Boundary

No wallet, orders, keys, capital, cron, Wukong, or Telegram action.
No changes to other modules.
No changes to bionicbanker.tech (separate site, separate repo).
Bionic Lab build and GitHub push only.
