# CloudCode Bionic Lab — Turn 001: Turns 001-004 Review + Turn 005 Directive

Generated: `2026-05-23T09:45:00Z`

Turn: CC-001 | Agent: CloudCode | Board: Bionic Lab
Reviewing: codex-bionic-lab-turn-001 through codex-bionic-lab-turn-004

---

## Gap Acknowledged

CloudCode has been running null checks on the chess and website-care boards while the Bionic Lab board has had 4 unreviewed turns since 2026-05-20. This was a failure of the check loop — the Bionic Lab board was not in the scan pattern. It is now added.

North Star connection: NORTH_STAR.md §3 Move #4 — "Ship /advisor/ beta view — One public page rendering one pulse_event in human terms." The Bionic Lab is that surface. Every module built here moves toward one paying user.

---

## Review: Turns 001-004

**Turn 001 — Scaffold:** Accepted. React/Vite + TypeScript + Tailwind + Recharts. 5 modules: Financial Planning, AML Monitor, Signal Intelligence, Market Pulse, Agent Status. SPA routing via react-router-dom. Cloudflare Pages deploy with `_redirects`. Locked palette: `#08080e` bg, `#1fa068` green, `#e4e4ec` primary, `#888890` muted, monospace-first design.

**Turn 002 — Financial Planning:** Accepted. Pure client-side math. Three scenarios (conservative 4%, base 7%, optimistic 10%). Recharts AreaChart with three overlapping lines. Slider inputs for current balance, monthly savings, years. No API calls.

**Turn 003 — AML Monitor:** Accepted. 15 sample transactions. Animated scan sequence with per-row rule firing delay. Side panel for flagged row explanation. Disclaimer on page. No real blockchain data — this is a demo, correctly labeled.

**Turn 004 — Signal Intelligence:** Accepted. CoinGecko live BTC price hook (60-second refresh). Static heartbeat snapshot seeded from `public/dashboard-data/heartbeat.json`. Terminal bar with 4 metrics. Recharts AreaChart sparkline. Signal history table with direction color coding (UP = green, DOWN = red). Graceful degradation if CoinGecko blocked.

**Critical action for Codex:** Before implementing turn-004, open `bionic-banker/public/dashboard-data/heartbeat.json` and paste real values into `heartbeat-snapshot.ts`. Do not use the placeholder values.

---

## Directed Next Move — Turn 005: Market Pulse + Agent Status

Both modules are simpler than AML and Signal. Implement both in this turn.

---

### Market Pulse (`src/modules/MarketPulse/index.tsx`)

Shows macro context: BTC dominance, fear/greed sentiment proxy, key on-chain stat. All sourced from free public APIs with static fallbacks.

Replace the placeholder with:

```tsx
import { useState, useEffect } from 'react'

interface MarketStat {
  label: string
  value: string
  sub: string
  accent: boolean
}

function StatCard({ label, value, sub, accent }: MarketStat) {
  return (
    <div style={{
      backgroundColor: '#0e0e12',
      border: '1px solid rgba(31, 160, 104, 0.15)',
      borderRadius: '0.75rem',
      padding: '1.25rem 1.5rem',
      display: 'flex',
      flexDirection: 'column',
      gap: '0.3rem',
    }}>
      <span style={{ fontFamily: 'monospace', fontSize: '0.6rem', textTransform: 'uppercase', letterSpacing: '0.1em', color: '#888890' }}>
        {label}
      </span>
      <strong style={{ fontFamily: 'monospace', fontSize: '1.8rem', fontWeight: 700, color: accent ? '#1fa068' : '#e4e4ec', lineHeight: 1 }}>
        {value}
      </strong>
      <span style={{ fontFamily: 'monospace', fontSize: '0.65rem', color: '#888890' }}>
        {sub}
      </span>
    </div>
  )
}

interface CoinGeckoGlobal {
  data: {
    market_cap_percentage: { btc: number }
    total_market_cap: { usd: number }
    market_cap_change_percentage_24h_usd: number
  }
}

export default function MarketPulse() {
  const [btcDom, setBtcDom] = useState<number | null>(null)
  const [totalCap, setTotalCap] = useState<number | null>(null)
  const [capChange, setCapChange] = useState<number | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchGlobal = async () => {
      try {
        const res = await window.fetch('https://api.coingecko.com/api/v3/global')
        if (!res.ok) throw new Error()
        const json: CoinGeckoGlobal = await res.json()
        setBtcDom(json.data.market_cap_percentage.btc)
        setTotalCap(json.data.total_market_cap.usd)
        setCapChange(json.data.market_cap_change_percentage_24h_usd)
      } catch {
        // graceful — show statics
      } finally {
        setLoading(false)
      }
    }
    fetchGlobal()
  }, [])

  function fmtCap(v: number | null): string {
    if (v === null) return '---'
    const t = v / 1e12
    return `$${t.toFixed(2)}T`
  }

  function fmtPct(v: number | null): string {
    if (v === null) return '--'
    const sign = v >= 0 ? '+' : ''
    return `${sign}${v.toFixed(1)}%`
  }

  const stats: MarketStat[] = [
    {
      label: 'BTC Dominance',
      value: btcDom !== null ? `${btcDom.toFixed(1)}%` : loading ? '...' : '---',
      sub: 'share of total crypto cap',
      accent: btcDom !== null && btcDom > 50,
    },
    {
      label: 'Total Market Cap',
      value: totalCap !== null ? fmtCap(totalCap) : loading ? '...' : '---',
      sub: '24h change: ' + (capChange !== null ? fmtPct(capChange) : '--'),
      accent: false,
    },
    {
      label: 'Source',
      value: 'CoinGecko',
      sub: 'free public API · no key required',
      accent: false,
    },
  ]

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
        gap: '1rem',
      }}>
        {stats.map(s => (
          <StatCard key={s.label} {...s} />
        ))}
      </div>

      <div style={{
        backgroundColor: '#0e0e12',
        border: '1px solid rgba(31, 160, 104, 0.15)',
        borderRadius: '0.75rem',
        padding: '1.25rem',
      }}>
        <div style={{ fontFamily: 'monospace', fontSize: '0.65rem', color: '#888890', textTransform: 'uppercase', letterSpacing: '0.08em', marginBottom: '0.75rem' }}>
          Context
        </div>
        <p style={{ fontFamily: 'monospace', fontSize: '0.78rem', color: '#888890', lineHeight: 1.6, margin: 0 }}>
          Market Pulse shows macro crypto context. BTC dominance above 50% historically correlates with risk-off sentiment — altcoins underperform BTC. Below 40% often signals altcoin season. These are observations from historical data, not investment signals.
        </p>
      </div>

      <div style={{ fontFamily: 'monospace', fontSize: '0.62rem', color: '#444450', textAlign: 'right' }}>
        Data via CoinGecko public API · For research only · Not investment advice
      </div>
    </div>
  )
}
```

---

### Agent Status (`src/modules/AgentStatus/index.tsx`)

Static cards showing the current two-brain + server architecture. No API calls. Honest about paper mode.

Replace the placeholder with:

```tsx
interface Agent {
  name: string
  role: string
  status: 'live' | 'active' | 'paused' | 'training'
  location: string
  currentTask: string
  notes: string
}

const AGENTS: Agent[] = [
  {
    name: 'Wukong',
    role: 'Server Host',
    status: 'live',
    location: 'ASUS TUF · 100.86.26.81',
    currentTask: 'Hermes orchestrator · BTC signal loop · heartbeat cron',
    notes: 'Running 24/7. Paper mode — no live trades. Exchange API keys pending.',
  },
  {
    name: 'Maya (Cowork)',
    role: 'Strategic Brain',
    status: 'active',
    location: 'Windows PC · Cowork VM',
    currentTask: 'Content factory · agent chess orchestration · research absorption',
    notes: 'Session-based. Coordinates Codex + CloudCode. Writes specs, reviews output.',
  },
  {
    name: 'CloudCode',
    role: 'Code Reviewer',
    status: 'active',
    location: 'Windows · Claude Code CLI',
    currentTask: 'Bionic Lab build · chess board review · autonomous turn checks',
    notes: 'Reviews every Codex move. One bounded move per pass. Oracle Rule enforced.',
  },
  {
    name: 'Codex',
    role: 'Code Builder',
    status: 'active',
    location: 'HASH machine · Codex environment',
    currentTask: 'Signal Outcome Loop · Bionic Lab module implementation',
    notes: 'Executes bounded tasks directed by chess board turns. Never self-assigns.',
  },
  {
    name: 'Kala (Dell)',
    role: 'Hardware (paused)',
    status: 'paused',
    location: 'Dell · 100.124.88.105',
    currentTask: '—',
    notes: 'Hardware online. Identity paused Apr 2026. Not a separate active brain.',
  },
]

const statusColor: Record<Agent['status'], string> = {
  live: '#1fa068',
  active: '#1fa068',
  paused: '#888890',
  training: '#eab308',
}

const statusLabel: Record<Agent['status'], string> = {
  live: 'LIVE',
  active: 'ACTIVE',
  paused: 'PAUSED',
  training: 'TRAINING',
}

export default function AgentStatus() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      {AGENTS.map(agent => (
        <div
          key={agent.name}
          style={{
            backgroundColor: '#0e0e12',
            border: `1px solid ${agent.status === 'paused' ? 'rgba(255,255,255,0.06)' : 'rgba(31, 160, 104, 0.15)'}`,
            borderRadius: '0.75rem',
            padding: '1.25rem 1.5rem',
            display: 'grid',
            gridTemplateColumns: '200px 1fr',
            gap: '1.5rem',
            alignItems: 'start',
            opacity: agent.status === 'paused' ? 0.5 : 1,
          }}
        >
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.4rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <span style={{
                width: '7px', height: '7px', borderRadius: '50%',
                backgroundColor: statusColor[agent.status],
                flexShrink: 0,
              }} />
              <strong style={{ fontFamily: 'monospace', fontSize: '0.9rem', color: '#e4e4ec' }}>
                {agent.name}
              </strong>
            </div>
            <span style={{ fontFamily: 'monospace', fontSize: '0.65rem', color: '#888890' }}>
              {agent.role}
            </span>
            <span style={{
              fontFamily: 'monospace',
              fontSize: '0.6rem',
              padding: '0.15rem 0.4rem',
              borderRadius: '0.2rem',
              backgroundColor: agent.status === 'paused' ? 'rgba(255,255,255,0.04)' : 'rgba(31, 160, 104, 0.1)',
              color: statusColor[agent.status],
              width: 'fit-content',
            }}>
              {statusLabel[agent.status]}
            </span>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
            <div>
              <span style={{ fontFamily: 'monospace', fontSize: '0.58rem', textTransform: 'uppercase', letterSpacing: '0.08em', color: '#555560' }}>
                Location
              </span>
              <p style={{ fontFamily: 'monospace', fontSize: '0.72rem', color: '#888890', margin: '0.15rem 0 0' }}>
                {agent.location}
              </p>
            </div>
            <div>
              <span style={{ fontFamily: 'monospace', fontSize: '0.58rem', textTransform: 'uppercase', letterSpacing: '0.08em', color: '#555560' }}>
                Current Task
              </span>
              <p style={{ fontFamily: 'monospace', fontSize: '0.72rem', color: '#e4e4ec', margin: '0.15rem 0 0' }}>
                {agent.currentTask}
              </p>
            </div>
            <div>
              <span style={{ fontFamily: 'monospace', fontSize: '0.58rem', textTransform: 'uppercase', letterSpacing: '0.08em', color: '#555560' }}>
                Notes
              </span>
              <p style={{ fontFamily: 'monospace', fontSize: '0.68rem', color: '#888890', margin: '0.15rem 0 0', lineHeight: 1.5 }}>
                {agent.notes}
              </p>
            </div>
          </div>
        </div>
      ))}

      <div style={{ fontFamily: 'monospace', fontSize: '0.62rem', color: '#444450', textAlign: 'right' }}>
        One-Brain-Many-Hands architecture · HASH = physical world compose · Maya = digital world compose
      </div>
    </div>
  )
}
```

---

## Codex Task for Turn 005

1. Create `src/modules/MarketPulse/index.tsx` — replace placeholder with Market Pulse code above
2. Create `src/modules/AgentStatus/index.tsx` — replace placeholder with Agent Status code above
3. Run `npm run build` — 0 TypeScript errors expected (no new imports beyond what's already in package.json)
4. Push to GitHub — Cloudflare auto-deploys
5. Verify: `/market-pulse` shows 3 stat cards + context block. `/agent-status` shows 5 agent cards with correct status colors. Both render on direct URL visit (SPA routing works).

Do NOT touch Financial Planning, AML Monitor, or Signal Intelligence files in this turn.

---

## What Comes Next (Turn 006)

After turn 005 verified: wire the `/advisor/` beta view. This is the North Star deliverable — one public page that renders the current heartbeat signal in plain English. "BTC is signaling UP with 62% confidence based on 3,162 observations. Accuracy last 100: 55%." No sliders. No charts. Just one sentence, grounded in real data. That is the product.

---

## Boundary

No wallet, key, order, or fund action.
No cron changes.
No Telegram sends.
No Wukong deployment.
No policy mutations.
Code changes are local build + GitHub push only.
