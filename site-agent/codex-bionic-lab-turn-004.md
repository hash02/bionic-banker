# Codex Bionic Lab — Turn 004: Signal Intelligence Module

Date: 2026-05-20
Actor: Codex
Written by: Claude
Depends on: Turn 001 deployed and verified

---

## What This Turn Does

Replaces the Signal Intelligence placeholder with a live data module.

Live BTC price via CoinGecko (same free API already used on bionicbanker.tech/intelligence). Prediction history from the heartbeat.json snapshot embedded in the app (static fallback if CORS blocks the live fetch). Recharts sparkline. Terminal bar with 4 live metrics.

---

## Files to Create / Replace

Three files total.

---

### `src/hooks/useCoinGecko.ts`

Create this new file:

```ts
import { useState, useEffect } from 'react'

interface CoinGeckoData {
  price: number | null
  change24h: number | null
  loading: boolean
  error: boolean
  lastFetched: string | null
}

export function useCoinGecko(): CoinGeckoData {
  const [state, setState] = useState<CoinGeckoData>({
    price: null,
    change24h: null,
    loading: true,
    error: false,
    lastFetched: null,
  })

  const fetch = async () => {
    try {
      const res = await window.fetch(
        'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true',
      )
      if (!res.ok) throw new Error('CoinGecko fetch failed')
      const data = await res.json()
      setState({
        price: data.bitcoin.usd,
        change24h: data.bitcoin.usd_24h_change,
        loading: false,
        error: false,
        lastFetched: new Date().toISOString(),
      })
    } catch {
      setState(prev => ({ ...prev, loading: false, error: true }))
    }
  }

  useEffect(() => {
    fetch()
    const interval = setInterval(fetch, 60_000)
    return () => clearInterval(interval)
  }, [])

  return state
}
```

---

### `src/data/heartbeat-snapshot.ts`

Create this new file. This is a static snapshot of the heartbeat.json data so the Signal Intelligence module works even if CORS blocks a live fetch. Codex should paste the actual current values from `bionic-banker/public/dashboard-data/heartbeat.json` into the `recentRows` array. The structure below shows the shape — replace the values with real ones from the file.

```ts
export interface HeartbeatRow {
  iso: string
  price_now: number
  direction: string
  confidence: number
}

export interface HeartbeatSnapshot {
  predictions_made: number
  accuracy_last_100: number
  mode: string
  generated_at: string
  last_direction: string
  last_confidence: number
  recent_rows: HeartbeatRow[]
}

// Paste real values from public/dashboard-data/heartbeat.json
// Replace these placeholders with actual data
export const HEARTBEAT_SNAPSHOT: HeartbeatSnapshot = {
  predictions_made: 3162,
  accuracy_last_100: 55,
  mode: 'LIVE',
  generated_at: '2026-05-20T09:47:00Z',
  last_direction: 'UP',
  last_confidence: 0.62,
  recent_rows: [
    // Paste up to 12 rows from heartbeat.json recentRows array
    // Each row should have: iso, price_now, direction, confidence
    // Example shape:
    // { iso: '2026-05-20T09:47:00Z', price_now: 104200, direction: 'UP', confidence: 0.62 },
  ],
}
```

**Important:** Before building, open `bionic-banker/public/dashboard-data/heartbeat.json` and copy the real `predictions_made`, `accuracy_last_100`, `mode`, `generated_at`, and the most recent 12 rows from the `recentRows` array into this file. Replace the placeholders above with real data.

---

### `src/modules/SignalIntelligence/index.tsx`

Replace entire file:

```tsx
import { useCoinGecko } from '../../hooks/useCoinGecko'
import { HEARTBEAT_SNAPSHOT } from '../../data/heartbeat-snapshot'
import SparklineChart from './SparklineChart'

function formatPrice(p: number | null): string {
  if (p === null) return '---'
  return `$${Math.round(p).toLocaleString('en-US')}`
}

function formatChange(c: number | null): string {
  if (c === null) return '--'
  const sign = c >= 0 ? '+' : ''
  return `${sign}${c.toFixed(2)}%`
}

function formatTime(iso: string): string {
  try {
    const d = new Date(iso)
    return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' }) +
      ' · ' +
      d.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: false })
  } catch {
    return iso
  }
}

export default function SignalIntelligence() {
  const btc = useCoinGecko()
  const hb = HEARTBEAT_SNAPSHOT
  const changePositive = btc.change24h !== null && btc.change24h >= 0

  const sparkPrices = hb.recent_rows.map(r => r.price_now)
  const sparkLabels = hb.recent_rows.map(r => formatTime(r.iso))

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>

      {/* Terminal bar */}
      <div style={{
        display: 'flex',
        backgroundColor: '#0e0e12',
        border: '1px solid rgba(31, 160, 104, 0.18)',
        borderRadius: '0.75rem',
        padding: '1.25rem 1.5rem',
        flexWrap: 'wrap',
        rowGap: '1rem',
      }}>
        {[
          {
            label: 'BTC Price',
            value: btc.loading ? 'Loading...' : btc.error ? 'Unavailable' : formatPrice(btc.price),
            sub: btc.change24h !== null
              ? `${formatChange(btc.change24h)} 24h`
              : 'live via CoinGecko',
            accent: !btc.error && !btc.loading,
          },
          {
            label: 'Signal Rows',
            value: hb.predictions_made.toLocaleString(),
            sub: 'total logged',
            accent: false,
          },
          {
            label: 'Last 100',
            value: `${hb.accuracy_last_100}%`,
            sub: 'accuracy',
            accent: hb.accuracy_last_100 >= 55,
          },
          {
            label: 'Last Read',
            value: hb.last_direction,
            sub: `${Math.round(hb.last_confidence * 100)}% confidence`,
            accent: false,
          },
        ].map(({ label, value, sub, accent }, i, arr) => (
          <div key={label} style={{ display: 'flex', alignItems: 'center', flex: '1 1 120px' }}>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.2rem', padding: '0 1rem' }}>
              <span style={{ fontFamily: 'monospace', fontSize: '0.6rem', textTransform: 'uppercase', letterSpacing: '0.1em', color: '#888890' }}>
                {label}
              </span>
              <strong style={{ fontFamily: 'monospace', fontSize: '1.35rem', fontWeight: 700, color: accent ? '#1fa068' : '#e4e4ec', lineHeight: 1.1 }}>
                {value}
              </strong>
              <span style={{ fontFamily: 'monospace', fontSize: '0.62rem', color: changePositive && label === 'BTC Price' ? '#1fa068' : '#888890' }}>
                {sub}
              </span>
            </div>
            {i < arr.length - 1 && (
              <div style={{ width: '1px', height: '2.5rem', backgroundColor: 'rgba(31, 160, 104, 0.1)', flexShrink: 0 }} />
            )}
          </div>
        ))}
      </div>

      {/* Sparkline */}
      {sparkPrices.length > 1 && (
        <div style={{
          backgroundColor: '#0e0e12',
          border: '1px solid rgba(31, 160, 104, 0.15)',
          borderRadius: '0.75rem',
          padding: '1.25rem',
        }}>
          <div style={{ fontFamily: 'monospace', fontSize: '0.65rem', color: '#888890', textTransform: 'uppercase', letterSpacing: '0.08em', marginBottom: '1rem' }}>
            BTC Price — Recent Snapshots
          </div>
          <SparklineChart prices={sparkPrices} labels={sparkLabels} />
        </div>
      )}

      {/* Recent rows table */}
      <div style={{
        backgroundColor: '#0e0e12',
        border: '1px solid rgba(31, 160, 104, 0.15)',
        borderRadius: '0.75rem',
        overflow: 'hidden',
      }}>
        <div style={{ padding: '1rem 1.25rem', borderBottom: '1px solid rgba(31, 160, 104, 0.08)' }}>
          <span style={{ fontFamily: 'monospace', fontSize: '0.65rem', color: '#888890', textTransform: 'uppercase', letterSpacing: '0.08em' }}>
            Signal History
          </span>
        </div>

        {/* Column headers */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: '2fr 1fr 1fr 1fr',
          padding: '0.5rem 1.25rem',
          backgroundColor: 'rgba(255,255,255,0.02)',
        }}>
          {['Timestamp', 'BTC Price', 'Direction', 'Confidence'].map(h => (
            <span key={h} style={{ fontFamily: 'monospace', fontSize: '0.58rem', textTransform: 'uppercase', letterSpacing: '0.1em', color: '#555560' }}>
              {h}
            </span>
          ))}
        </div>

        {hb.recent_rows.length === 0 ? (
          <div style={{ padding: '2rem 1.25rem', fontFamily: 'monospace', fontSize: '0.75rem', color: '#555560', textAlign: 'center' }}>
            No snapshot rows loaded. Add real rows to heartbeat-snapshot.ts.
          </div>
        ) : (
          hb.recent_rows.slice().reverse().map((row, i) => (
            <div
              key={i}
              style={{
                display: 'grid',
                gridTemplateColumns: '2fr 1fr 1fr 1fr',
                padding: '0.65rem 1.25rem',
                borderTop: i > 0 ? '1px solid rgba(255,255,255,0.03)' : 'none',
                transition: 'background 0.15s',
              }}
            >
              <span style={{ fontFamily: 'monospace', fontSize: '0.72rem', color: '#888890' }}>
                {formatTime(row.iso)}
              </span>
              <span style={{ fontFamily: 'monospace', fontSize: '0.78rem', color: '#e4e4ec' }}>
                {formatPrice(row.price_now)}
              </span>
              <span style={{
                fontFamily: 'monospace',
                fontSize: '0.72rem',
                fontWeight: 600,
                color: row.direction === 'UP' ? '#1fa068' : row.direction === 'DOWN' ? '#e55' : '#888890',
              }}>
                {row.direction}
              </span>
              <span style={{ fontFamily: 'monospace', fontSize: '0.72rem', color: '#888890' }}>
                {Math.round(row.confidence * 100)}%
              </span>
            </div>
          ))
        )}
      </div>

      {/* Mode + disclaimer */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <span style={{
          fontFamily: 'monospace',
          fontSize: '0.65rem',
          color: '#1fa068',
          display: 'flex',
          alignItems: 'center',
          gap: '0.4rem',
        }}>
          <span style={{ width: '6px', height: '6px', borderRadius: '50%', backgroundColor: '#1fa068', display: 'inline-block' }} />
          {hb.mode} — {formatTime(hb.generated_at)}
        </span>
        <p style={{ fontFamily: 'monospace', fontSize: '0.62rem', color: '#444450', margin: 0 }}>
          For research only. Not investment advice. Not trading performance.
        </p>
      </div>
    </div>
  )
}
```

---

### `src/modules/SignalIntelligence/SparklineChart.tsx`

Create this new file:

```tsx
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from 'recharts'

interface Props {
  prices: number[]
  labels: string[]
}

function fmt(v: number): string {
  return `$${Math.round(v).toLocaleString('en-US')}`
}

export default function SparklineChart({ prices, labels }: Props) {
  const data = prices.map((price, i) => ({ label: labels[i], price }))

  return (
    <ResponsiveContainer width="100%" height={100}>
      <AreaChart data={data} margin={{ top: 4, right: 8, left: 8, bottom: 0 }}>
        <defs>
          <linearGradient id="sparkFill" x1="0" y1="0" x2="0" y2="1">
            <stop offset="5%" stopColor="#1fa068" stopOpacity={0.25} />
            <stop offset="95%" stopColor="#1fa068" stopOpacity={0.02} />
          </linearGradient>
        </defs>
        <XAxis
          dataKey="label"
          tick={{ fontFamily: 'monospace', fontSize: 9, fill: '#555560' }}
          axisLine={false}
          tickLine={false}
          interval="preserveStartEnd"
        />
        <YAxis hide domain={['auto', 'auto']} />
        <Tooltip
          contentStyle={{
            backgroundColor: '#0e0e12',
            border: '1px solid rgba(31, 160, 104, 0.2)',
            borderRadius: '6px',
            fontFamily: 'monospace',
            fontSize: '0.72rem',
            color: '#e4e4ec',
          }}
          formatter={(value: number) => [fmt(value), 'BTC']}
          labelStyle={{ color: '#888890', marginBottom: '0.2rem' }}
        />
        <Area
          type="monotone"
          dataKey="price"
          stroke="#1fa068"
          strokeWidth={2}
          fill="url(#sparkFill)"
          dot={{ fill: '#1fa068', strokeWidth: 0, r: 3 }}
          activeDot={{ fill: '#1fa068', strokeWidth: 0, r: 5 }}
        />
      </AreaChart>
    </ResponsiveContainer>
  )
}
```

---

## Step 1: Read heartbeat.json First

Before creating any files, open:
```
bionic-banker/public/dashboard-data/heartbeat.json
```

Read the current values and paste them into `heartbeat-snapshot.ts`:
- `predictions_made` number
- `accuracy_last_100` number (as integer, e.g. 55 not 0.55)
- `mode` string
- `generated_at` ISO string
- `last_direction` string (UP/DOWN/NEUTRAL)
- `last_confidence` float (0 to 1)
- `recent_rows` — paste up to 12 rows from the `recentRows` array. Each needs `iso`, `price_now`, `direction`, `confidence`.

---

## Step 2: Create / Replace Files

- Create `src/hooks/useCoinGecko.ts`
- Create `src/data/heartbeat-snapshot.ts` (with real values from heartbeat.json)
- Replace `src/modules/SignalIntelligence/index.tsx`
- Create `src/modules/SignalIntelligence/SparklineChart.tsx`

---

## Step 3: Build and Deploy

```bash
npm run build
```

Push to GitHub — Cloudflare Pages auto-deploys.

---

## Step 4: Verify

- Navigate to `/signal-intelligence`
- Terminal bar shows: BTC price (live, green), signal rows count, last-100 accuracy, last direction
- BTC price refreshes every 60 seconds automatically (check console for fetch calls)
- Recharts sparkline renders with the snapshot price history
- Signal history table shows rows in reverse chronological order (newest first)
- Direction column: UP = green, DOWN = red
- Mode indicator at bottom left shows LIVE + timestamp
- Disclaimer at bottom right
- If CoinGecko is down or CORS blocked: BTC price shows "Unavailable" gracefully — rest of module still works

---

## What Comes Next

Turn 005: Market Pulse + Agent Status modules. Both simpler than AML and Signal — Market Pulse uses existing DeFi JSON data structure, Agent Status is static cards.
