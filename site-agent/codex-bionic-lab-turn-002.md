# Codex Bionic Lab — Turn 002: Financial Planning Module

Date: 2026-05-20
Actor: Codex
Written by: Claude
Depends on: Turn 001 deployed and verified

---

## What This Turn Does

Replaces the Financial Planning placeholder with a fully working interactive calculator.

Pure client-side math. No API calls. No backend. User adjusts inputs and the projection chart updates live.

---

## Files to Replace / Create

Replace the placeholder and add the chart component. Two files total.

---

### `src/modules/FinancialPlanning/index.tsx`

Replace the entire file with:

```tsx
import { useState, useMemo } from 'react'
import ProjectionChart from './ProjectionChart'

const SCENARIOS = {
  conservative: 0.04,
  base: 0.07,
  optimistic: 0.10,
}

function projectBalance(
  currentBalance: number,
  monthlySavings: number,
  annualRate: number,
  years: number,
): number[] {
  const monthlyRate = annualRate / 12
  const points: number[] = []
  let balance = currentBalance
  for (let y = 0; y <= years; y++) {
    points.push(Math.round(balance))
    for (let m = 0; m < 12; m++) {
      balance = balance * (1 + monthlyRate) + monthlySavings
    }
  }
  return points
}

function formatCAD(n: number): string {
  if (n >= 1_000_000) return `$${(n / 1_000_000).toFixed(2)}M`
  if (n >= 1_000) return `$${(n / 1_000).toFixed(0)}K`
  return `$${n.toLocaleString()}`
}

export default function FinancialPlanning() {
  const [balance, setBalance] = useState(25000)
  const [monthly, setMonthly] = useState(1000)
  const [years, setYears] = useState(20)
  const [goal, setGoal] = useState(500000)

  const projections = useMemo(() => {
    const labels = Array.from({ length: years + 1 }, (_, i) => `Y${i}`)
    return {
      labels,
      conservative: projectBalance(balance, monthly, SCENARIOS.conservative, years),
      base: projectBalance(balance, monthly, SCENARIOS.base, years),
      optimistic: projectBalance(balance, monthly, SCENARIOS.optimistic, years),
    }
  }, [balance, monthly, years])

  const finalBase = projections.base[projections.base.length - 1]
  const gap = goal - finalBase
  const yearsToGoal = useMemo(() => {
    let b = balance
    const mr = SCENARIOS.base / 12
    for (let m = 0; m < years * 12; m++) {
      b = b * (1 + mr) + monthly
      if (b >= goal) return Math.ceil(m / 12)
    }
    return null
  }, [balance, monthly, goal, years])

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>

      {/* Terminal bar */}
      <div style={{
        display: 'flex',
        gap: 0,
        backgroundColor: '#0e0e12',
        border: '1px solid rgba(31, 160, 104, 0.18)',
        borderRadius: '0.75rem',
        padding: '1.25rem 1.5rem',
        flexWrap: 'wrap',
        rowGap: '1rem',
      }}>
        {[
          { label: 'Projected (Base)', value: formatCAD(finalBase), sub: `at ${years}yr, 7% return` },
          { label: 'Goal Gap', value: gap > 0 ? `${formatCAD(gap)} short` : 'Goal reached', sub: gap > 0 ? 'at base scenario' : 'at base scenario', accent: gap <= 0 },
          { label: 'Years to Goal', value: yearsToGoal !== null ? `${yearsToGoal} yrs` : `>${years} yrs`, sub: 'base scenario, 7% return', accent: yearsToGoal !== null && yearsToGoal <= years },
          { label: 'Monthly Input', value: `$${monthly.toLocaleString()}`, sub: 'savings per month' },
        ].map(({ label, value, sub, accent }, i, arr) => (
          <div key={label} style={{ display: 'flex', alignItems: 'center', flex: '1 1 120px' }}>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.2rem', padding: '0 1rem' }}>
              <span style={{ fontFamily: 'monospace', fontSize: '0.6rem', textTransform: 'uppercase', letterSpacing: '0.1em', color: '#888890' }}>
                {label}
              </span>
              <strong style={{ fontFamily: 'monospace', fontSize: '1.35rem', fontWeight: 700, color: accent ? '#1fa068' : '#e4e4ec', lineHeight: 1.1 }}>
                {value}
              </strong>
              <span style={{ fontFamily: 'monospace', fontSize: '0.62rem', color: '#888890' }}>{sub}</span>
            </div>
            {i < arr.length - 1 && (
              <div style={{ width: '1px', height: '2.5rem', backgroundColor: 'rgba(31, 160, 104, 0.12)', flexShrink: 0 }} />
            )}
          </div>
        ))}
      </div>

      {/* Chart */}
      <div style={{
        backgroundColor: '#0e0e12',
        border: '1px solid rgba(31, 160, 104, 0.15)',
        borderRadius: '0.75rem',
        padding: '1.25rem',
      }}>
        <div style={{ fontFamily: 'monospace', fontSize: '0.65rem', color: '#888890', textTransform: 'uppercase', letterSpacing: '0.08em', marginBottom: '1rem' }}>
          Balance Projection
        </div>
        <ProjectionChart
          labels={projections.labels}
          conservative={projections.conservative}
          base={projections.base}
          optimistic={projections.optimistic}
        />
        <div style={{ display: 'flex', gap: '1.5rem', marginTop: '0.75rem', paddingLeft: '0.5rem' }}>
          {[
            { label: 'Conservative (4%)', color: 'rgba(31,160,104,0.35)' },
            { label: 'Base (7%)', color: '#1fa068' },
            { label: 'Optimistic (10%)', color: 'rgba(31,160,104,0.7)' },
          ].map(({ label, color }) => (
            <span key={label} style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', fontFamily: 'monospace', fontSize: '0.65rem', color: '#888890' }}>
              <span style={{ width: '1.5rem', height: '2px', backgroundColor: color, display: 'inline-block', borderRadius: '1px' }} />
              {label}
            </span>
          ))}
        </div>
      </div>

      {/* Inputs */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))',
        gap: '1rem',
      }}>
        {[
          { label: 'Current Balance', value: balance, setter: setBalance, min: 0, max: 500000, step: 1000, format: (v: number) => `$${v.toLocaleString()}` },
          { label: 'Monthly Savings', value: monthly, setter: setMonthly, min: 100, max: 10000, step: 100, format: (v: number) => `$${v.toLocaleString()}` },
          { label: 'Time Horizon', value: years, setter: setYears, min: 1, max: 40, step: 1, format: (v: number) => `${v} years` },
          { label: 'Goal', value: goal, setter: setGoal, min: 10000, max: 2000000, step: 10000, format: (v: number) => formatCAD(v) },
        ].map(({ label, value, setter, min, max, step, format }) => (
          <div key={label} style={{
            backgroundColor: '#0e0e12',
            border: '1px solid rgba(31, 160, 104, 0.15)',
            borderRadius: '0.75rem',
            padding: '1rem 1.25rem',
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.6rem' }}>
              <span style={{ fontFamily: 'monospace', fontSize: '0.65rem', textTransform: 'uppercase', letterSpacing: '0.08em', color: '#888890' }}>
                {label}
              </span>
              <span style={{ fontFamily: 'monospace', fontSize: '0.78rem', color: '#1fa068', fontWeight: 600 }}>
                {format(value)}
              </span>
            </div>
            <input
              type="range"
              min={min}
              max={max}
              step={step}
              value={value}
              onChange={(e) => setter(Number(e.target.value))}
              style={{
                width: '100%',
                accentColor: '#1fa068',
                cursor: 'pointer',
              }}
            />
          </div>
        ))}
      </div>

      {/* Disclaimer */}
      <p style={{ fontFamily: 'monospace', fontSize: '0.65rem', color: '#555560', textAlign: 'center', margin: 0 }}>
        For illustration only. Not financial advice. Returns are not guaranteed.
      </p>
    </div>
  )
}
```

---

### `src/modules/FinancialPlanning/ProjectionChart.tsx`

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
  labels: string[]
  conservative: number[]
  base: number[]
  optimistic: number[]
}

function fmt(v: number): string {
  if (v >= 1_000_000) return `$${(v / 1_000_000).toFixed(1)}M`
  if (v >= 1_000) return `$${(v / 1_000).toFixed(0)}K`
  return `$${v}`
}

export default function ProjectionChart({ labels, conservative, base, optimistic }: Props) {
  const data = labels.map((label, i) => ({
    label,
    conservative: conservative[i],
    base: base[i],
    optimistic: optimistic[i],
  }))

  return (
    <ResponsiveContainer width="100%" height={220}>
      <AreaChart data={data} margin={{ top: 4, right: 8, left: 8, bottom: 0 }}>
        <defs>
          <linearGradient id="fillOptimistic" x1="0" y1="0" x2="0" y2="1">
            <stop offset="5%" stopColor="#1fa068" stopOpacity={0.15} />
            <stop offset="95%" stopColor="#1fa068" stopOpacity={0} />
          </linearGradient>
          <linearGradient id="fillBase" x1="0" y1="0" x2="0" y2="1">
            <stop offset="5%" stopColor="#1fa068" stopOpacity={0.25} />
            <stop offset="95%" stopColor="#1fa068" stopOpacity={0.02} />
          </linearGradient>
          <linearGradient id="fillConservative" x1="0" y1="0" x2="0" y2="1">
            <stop offset="5%" stopColor="#1fa068" stopOpacity={0.08} />
            <stop offset="95%" stopColor="#1fa068" stopOpacity={0} />
          </linearGradient>
        </defs>
        <XAxis
          dataKey="label"
          tick={{ fontFamily: 'monospace', fontSize: 10, fill: '#555560' }}
          axisLine={false}
          tickLine={false}
          interval="preserveStartEnd"
        />
        <YAxis
          tickFormatter={fmt}
          tick={{ fontFamily: 'monospace', fontSize: 10, fill: '#555560' }}
          axisLine={false}
          tickLine={false}
          width={52}
        />
        <Tooltip
          contentStyle={{
            backgroundColor: '#0e0e12',
            border: '1px solid rgba(31, 160, 104, 0.2)',
            borderRadius: '6px',
            fontFamily: 'monospace',
            fontSize: '0.72rem',
            color: '#e4e4ec',
          }}
          labelStyle={{ color: '#888890', marginBottom: '0.25rem' }}
          formatter={(value: number, name: string) => [fmt(value), name.charAt(0).toUpperCase() + name.slice(1)]}
        />
        <Area type="monotone" dataKey="optimistic" stroke="rgba(31,160,104,0.5)" strokeWidth={1.5} fill="url(#fillOptimistic)" strokeDasharray="4 2" />
        <Area type="monotone" dataKey="base" stroke="#1fa068" strokeWidth={2} fill="url(#fillBase)" />
        <Area type="monotone" dataKey="conservative" stroke="rgba(31,160,104,0.35)" strokeWidth={1.5} fill="url(#fillConservative)" strokeDasharray="2 2" />
      </AreaChart>
    </ResponsiveContainer>
  )
}
```

---

## Step 1: Copy Both Files

Replace `src/modules/FinancialPlanning/index.tsx` and create `src/modules/FinancialPlanning/ProjectionChart.tsx`.

---

## Step 2: Build and Deploy

```bash
npm run build
```

Expected: 0 errors. If Recharts type errors appear, they are safe to ignore (Recharts v2 has some loose typings). Do not add `@ts-ignore` unless the build actually fails.

Push to GitHub — Cloudflare Pages auto-deploys.

---

## Step 3: Verify

- Navigate to `/financial-planning` in the deployed app
- Terminal bar shows 4 metrics: projected balance, gap, years to goal, monthly input
- Recharts area chart renders with 3 lines (conservative/base/optimistic)
- Moving any slider updates the chart and metrics in real time
- Mobile at 375px: inputs stack vertically, chart remains readable
- Disclaimer visible at bottom

---

## What Comes Next

Turn 003: AML Monitor module — 15 sample transactions, rule-firing engine, side panel with rule explanation.
