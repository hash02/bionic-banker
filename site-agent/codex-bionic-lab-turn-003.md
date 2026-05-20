# Codex Bionic Lab — Turn 003: AML Monitor Module

Date: 2026-05-20
Actor: Codex
Written by: Claude
Depends on: Turn 001 deployed and verified

---

## What This Turn Does

Replaces the AML Monitor placeholder with a fully working transaction scanner demo.

15 sample transactions. User clicks Scan. Rules fire one by one across each row with a short delay — feels like a real engine running. Click any flagged row and a side panel explains exactly which rules triggered and why.

No real blockchain data. This is a demo. Disclaimer is on the page.

---

## Files to Create / Replace

Four files total.

---

### `src/data/aml-sample-transactions.ts`

Create this new file:

```ts
export type RuleSeverity = 'low' | 'medium' | 'high'

export interface RuleTrigger {
  code: string
  label: string
  severity: RuleSeverity
  explanation: string
}

export interface Transaction {
  id: string
  hash: string
  from: string
  to: string
  amount: number
  currency: string
  timestamp: string
  riskScore: number
  rules: RuleTrigger[]
}

export const SAMPLE_TRANSACTIONS: Transaction[] = [
  {
    id: 'tx-001',
    hash: '0x4a9f...2c1d',
    from: '0x742d35Cc6634C0532925a3b8D4C9C8',
    to: '0x1a2b3c4d5e6f7890abcdef12345678',
    amount: 9900,
    currency: 'USDC',
    timestamp: '2026-05-20 14:22:11',
    riskScore: 78,
    rules: [
      {
        code: 'threshold_structuring',
        label: 'Threshold Structuring',
        severity: 'high',
        explanation: 'Amount of $9,900 USDC falls $100 below the $10,000 FINTRAC reporting threshold. Same address has sent $9,800, $9,750, and $9,900 within 7 days. Classic structuring pattern.',
      },
    ],
  },
  {
    id: 'tx-002',
    hash: '0x7b3a...8e4f',
    from: '0x9f8e7d6c5b4a3210fedcba987654321',
    to: '0x2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e',
    amount: 48500,
    currency: 'ETH',
    timestamp: '2026-05-20 11:08:45',
    riskScore: 91,
    rules: [
      {
        code: 'mixer_touch',
        label: 'Mixer Touch',
        severity: 'high',
        explanation: 'Funds trace back 2 hops to Tornado Cash contract 0xd90e2...f3c1. Mixer contact within the last 72 hours. High confidence attribution.',
      },
      {
        code: 'sanctions_proximity',
        label: 'Sanctions Proximity',
        severity: 'high',
        explanation: 'Sending address co-transacted with 0x7F367...b4C9 which appears on OFAC SDN list (Lazarus Group cluster). Distance: 1 hop.',
      },
    ],
  },
  {
    id: 'tx-003',
    hash: '0x1c8d...a2b7',
    from: '0x3e4f5a6b7c8d9e0f1a2b3c4d5e6f70',
    to: '0x4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b',
    amount: 1250,
    currency: 'USDC',
    timestamp: '2026-05-20 09:14:33',
    riskScore: 8,
    rules: [],
  },
  {
    id: 'tx-004',
    hash: '0x9d2e...f5c8',
    from: '0x5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c',
    to: '0x6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d',
    amount: 312000,
    currency: 'USDT',
    timestamp: '2026-05-19 23:47:02',
    riskScore: 62,
    rules: [
      {
        code: 'timing_anomaly',
        label: 'Timing Anomaly',
        severity: 'medium',
        explanation: 'Transaction sent at 23:47 local time. Address has 94% of prior transactions between 09:00-17:00. Off-hours transaction combined with amount exceeding $300K triggers review threshold.',
      },
      {
        code: 'fan_in_pattern',
        label: 'Fan-In Pattern',
        severity: 'medium',
        explanation: 'Destination address received funds from 14 unique wallets in the 48 hours prior to this transaction. Aggregate inflow: $1.2M. Fan-in patterns precede layering in 38% of confirmed cases.',
      },
    ],
  },
  {
    id: 'tx-005',
    hash: '0x2f7b...4d9a',
    from: '0x7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e',
    to: '0x8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f',
    amount: 450,
    currency: 'USDC',
    timestamp: '2026-05-19 16:30:18',
    riskScore: 5,
    rules: [],
  },
  {
    id: 'tx-006',
    hash: '0x6a1c...b8e3',
    from: '0x9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a',
    to: '0x0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b',
    amount: 9500,
    currency: 'USDC',
    timestamp: '2026-05-19 14:12:57',
    riskScore: 55,
    rules: [
      {
        code: 'threshold_structuring',
        label: 'Threshold Structuring',
        severity: 'medium',
        explanation: 'Amount of $9,500 USDC is below the $10,000 reporting threshold. Single occurrence — flagged for monitoring. Escalates to high if pattern repeats within 30 days.',
      },
    ],
  },
  {
    id: 'tx-007',
    hash: '0x3e9d...c7f2',
    from: '0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c',
    to: '0x2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d',
    amount: 8750,
    currency: 'ETH',
    timestamp: '2026-05-19 10:55:30',
    riskScore: 12,
    rules: [],
  },
  {
    id: 'tx-008',
    hash: '0x8b4f...d1a6',
    from: '0x3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e',
    to: '0x4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f',
    amount: 125000,
    currency: 'USDT',
    timestamp: '2026-05-18 22:03:14',
    riskScore: 84,
    rules: [
      {
        code: 'mixer_touch',
        label: 'Mixer Touch',
        severity: 'high',
        explanation: 'Source funds passed through ChipMixer — a now-sanctioned mixing service seized by law enforcement in 2023. Historical mixer touch is still flagged under current guidance.',
      },
      {
        code: 'timing_anomaly',
        label: 'Timing Anomaly',
        severity: 'medium',
        explanation: 'Sent at 22:03. Address has no prior after-hours transactions across 180-day history. Combined with mixer touch, escalates overall risk score.',
      },
    ],
  },
  {
    id: 'tx-009',
    hash: '0x5c2a...e9b4',
    from: '0x5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a',
    to: '0x6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b',
    amount: 3200,
    currency: 'USDC',
    timestamp: '2026-05-18 15:40:22',
    riskScore: 4,
    rules: [],
  },
  {
    id: 'tx-010',
    hash: '0x0d7f...3c8e',
    from: '0x7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c',
    to: '0x8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d',
    amount: 750000,
    currency: 'USDT',
    timestamp: '2026-05-18 08:17:59',
    riskScore: 96,
    rules: [
      {
        code: 'sanctions_proximity',
        label: 'Sanctions Proximity',
        severity: 'high',
        explanation: 'Sending address is 0 hops from 0x8576...c4F2, a directly sanctioned entity on the OFAC SDN list. Direct counterparty contact. Automatic escalation.',
      },
      {
        code: 'fan_in_pattern',
        label: 'Fan-In Pattern',
        severity: 'high',
        explanation: 'Sending address received from 31 unique wallets in the 24 hours prior. Aggregate inflow: $3.1M across 31 transactions, then consolidated into this single $750K outflow. Classic layering structure.',
      },
      {
        code: 'mixer_touch',
        label: 'Mixer Touch',
        severity: 'high',
        explanation: 'Source of funds traces to Tornado Cash pool via 3-hop path. Attribution confidence: 87% using heuristic clustering.',
      },
    ],
  },
  {
    id: 'tx-011',
    hash: '0x1e4b...7a9c',
    from: '0x9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e',
    to: '0x0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f',
    amount: 18400,
    currency: 'USDC',
    timestamp: '2026-05-17 13:28:44',
    riskScore: 22,
    rules: [
      {
        code: 'timing_anomaly',
        label: 'Timing Anomaly',
        severity: 'low',
        explanation: 'Transaction on a public holiday. Low-severity flag. Address has sent on holidays before. No other indicators present. Monitor only.',
      },
    ],
  },
  {
    id: 'tx-012',
    hash: '0x7f3c...2b5d',
    from: '0x1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a',
    to: '0x2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b',
    amount: 560,
    currency: 'ETH',
    timestamp: '2026-05-17 11:05:08',
    riskScore: 7,
    rules: [],
  },
  {
    id: 'tx-013',
    hash: '0x4a8e...6d1f',
    from: '0x3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c',
    to: '0x4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d',
    amount: 9800,
    currency: 'USDT',
    timestamp: '2026-05-16 18:44:31',
    riskScore: 71,
    rules: [
      {
        code: 'threshold_structuring',
        label: 'Threshold Structuring',
        severity: 'high',
        explanation: 'Third transaction in 14 days from this address below the $10,000 reporting threshold: $9,900 on May 6, $9,750 on May 12, $9,800 today. Pattern meets the FINTRAC structuring definition. SAR filing recommended.',
      },
    ],
  },
  {
    id: 'tx-014',
    hash: '0x2c6d...9e3a',
    from: '0x5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e',
    to: '0x6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f',
    amount: 2100,
    currency: 'USDC',
    timestamp: '2026-05-16 09:20:17',
    riskScore: 3,
    rules: [],
  },
  {
    id: 'tx-015',
    hash: '0x9b5a...1f4c',
    from: '0x7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a',
    to: '0x8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b',
    amount: 88000,
    currency: 'ETH',
    timestamp: '2026-05-15 20:33:52',
    riskScore: 68,
    rules: [
      {
        code: 'fan_in_pattern',
        label: 'Fan-In Pattern',
        severity: 'medium',
        explanation: 'Destination wallet received from 8 separate wallets in the 6 hours before this transfer. Aggregate inflow: $425K. Possible consolidation before movement.',
      },
      {
        code: 'timing_anomaly',
        label: 'Timing Anomaly',
        severity: 'medium',
        explanation: 'Sent at 20:33 on a Friday. Address has a strong weekday 09:00-17:00 pattern across 90-day history. Off-pattern timing combined with fan-in activity warrants review.',
      },
    ],
  },
]

export const RULE_META: Record<string, { color: string; bg: string }> = {
  mixer_touch: { color: '#e55', bg: 'rgba(220,50,50,0.1)' },
  sanctions_proximity: { color: '#e55', bg: 'rgba(220,50,50,0.1)' },
  fan_in_pattern: { color: '#eab308', bg: 'rgba(234,179,8,0.1)' },
  timing_anomaly: { color: '#888890', bg: 'rgba(136,136,144,0.1)' },
  threshold_structuring: { color: '#eab308', bg: 'rgba(234,179,8,0.1)' },
}
```

---

### `src/modules/AMLMonitor/index.tsx`

Replace entire file:

```tsx
import { useState } from 'react'
import { SAMPLE_TRANSACTIONS, Transaction } from '../../data/aml-sample-transactions'
import TransactionRow from './TransactionRow'
import RulePanel from './RulePanel'

const BLANK = SAMPLE_TRANSACTIONS.map(tx => ({ ...tx, rules: [], riskScore: 0 }))

export default function AMLMonitor() {
  const [txs, setTxs] = useState<Transaction[]>(BLANK)
  const [scanning, setScanning] = useState(false)
  const [scanned, setScanned] = useState(false)
  const [selected, setSelected] = useState<Transaction | null>(null)

  const handleScan = () => {
    if (scanning) return
    setScanning(true)
    setScanned(false)
    setSelected(null)
    setTxs(BLANK)

    SAMPLE_TRANSACTIONS.forEach((tx, i) => {
      setTimeout(() => {
        setTxs(prev => prev.map(t => (t.id === tx.id ? tx : t)))
        if (i === SAMPLE_TRANSACTIONS.length - 1) {
          setScanning(false)
          setScanned(true)
        }
      }, i * 120)
    })
  }

  const flagged = txs.filter(t => t.rules.length > 0).length
  const clean = txs.filter(t => scanned && t.rules.length === 0).length
  const rulesRun = scanned ? SAMPLE_TRANSACTIONS.reduce((acc, tx) => acc + 5, 0) : 0

  return (
    <div style={{ display: 'flex', gap: '1.25rem', height: '100%' }}>

      {/* Main panel */}
      <div style={{ flex: 1, minWidth: 0, display: 'flex', flexDirection: 'column', gap: '1rem' }}>

        {/* Header bar */}
        <div style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          backgroundColor: '#0e0e12',
          border: '1px solid rgba(31, 160, 104, 0.15)',
          borderRadius: '0.75rem',
          padding: '1rem 1.25rem',
          flexWrap: 'wrap',
          gap: '1rem',
        }}>
          <div style={{ display: 'flex', gap: '2rem', flexWrap: 'wrap' }}>
            {[
              { label: 'Transactions', value: String(SAMPLE_TRANSACTIONS.length) },
              { label: 'Rules Run', value: scanned ? String(rulesRun) : '--' },
              { label: 'Flagged', value: scanned ? String(flagged) : '--', accent: flagged > 0 && scanned },
              { label: 'Clean', value: scanned ? String(clean) : '--' },
            ].map(({ label, value, accent }) => (
              <div key={label} style={{ display: 'flex', flexDirection: 'column', gap: '0.15rem' }}>
                <span style={{ fontFamily: 'monospace', fontSize: '0.58rem', textTransform: 'uppercase', letterSpacing: '0.1em', color: '#888890' }}>
                  {label}
                </span>
                <strong style={{ fontFamily: 'monospace', fontSize: '1.2rem', fontWeight: 700, color: accent ? '#1fa068' : '#e4e4ec' }}>
                  {value}
                </strong>
              </div>
            ))}
          </div>

          <button
            onClick={handleScan}
            disabled={scanning}
            style={{
              fontFamily: 'monospace',
              fontSize: '0.75rem',
              fontWeight: 600,
              padding: '0.6rem 1.25rem',
              borderRadius: '0.5rem',
              border: '1px solid #1fa068',
              backgroundColor: scanning ? 'rgba(31, 160, 104, 0.1)' : '#1fa068',
              color: scanning ? '#1fa068' : '#08080e',
              cursor: scanning ? 'not-allowed' : 'pointer',
              transition: 'all 0.15s',
              letterSpacing: '0.06em',
            }}
          >
            {scanning ? 'Scanning...' : scanned ? 'Re-Scan' : 'Run Scan'}
          </button>
        </div>

        {/* Column headers */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: '2fr 1fr 1fr 1fr 2fr',
          padding: '0 1rem',
          gap: '0.5rem',
        }}>
          {['Hash', 'Amount', 'Currency', 'Risk', 'Rules'].map(h => (
            <span key={h} style={{ fontFamily: 'monospace', fontSize: '0.6rem', textTransform: 'uppercase', letterSpacing: '0.1em', color: '#555560' }}>
              {h}
            </span>
          ))}
        </div>

        {/* Transaction rows */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.4rem', overflowY: 'auto' }}>
          {txs.map(tx => (
            <TransactionRow
              key={tx.id}
              tx={tx}
              scanned={scanned || scanning}
              selected={selected?.id === tx.id}
              onClick={() => setSelected(selected?.id === tx.id ? null : tx)}
            />
          ))}
        </div>

        {/* Disclaimer */}
        <p style={{ fontFamily: 'monospace', fontSize: '0.62rem', color: '#444450', margin: 0, textAlign: 'center' }}>
          Demo data only. Not connected to live blockchain. Not compliance advice.
        </p>
      </div>

      {/* Side panel */}
      {selected && (
        <RulePanel tx={selected} onClose={() => setSelected(null)} />
      )}
    </div>
  )
}
```

---

### `src/modules/AMLMonitor/TransactionRow.tsx`

Create this new file:

```tsx
import { Transaction, RULE_META } from '../../data/aml-sample-transactions'

interface Props {
  tx: Transaction
  scanned: boolean
  selected: boolean
  onClick: () => void
}

function RiskBar({ score }: { score: number }) {
  const color = score >= 70 ? '#e55' : score >= 40 ? '#eab308' : '#1fa068'
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
      <div style={{ flex: 1, height: '4px', backgroundColor: 'rgba(255,255,255,0.06)', borderRadius: '2px', maxWidth: '60px' }}>
        <div style={{ width: `${score}%`, height: '100%', backgroundColor: color, borderRadius: '2px', transition: 'width 0.4s ease' }} />
      </div>
      <span style={{ fontFamily: 'monospace', fontSize: '0.7rem', color, minWidth: '2rem' }}>
        {scanned || score > 0 ? score : '--'}
      </span>
    </div>
  )
}

function scanned_placeholder(scanned: boolean) {
  return !scanned
}

export default function TransactionRow({ tx, scanned, selected, onClick }: Props) {
  const hasRules = tx.rules.length > 0
  const borderColor = selected
    ? '#1fa068'
    : hasRules
    ? 'rgba(220, 50, 50, 0.25)'
    : 'rgba(31, 160, 104, 0.1)'

  return (
    <div
      onClick={onClick}
      style={{
        display: 'grid',
        gridTemplateColumns: '2fr 1fr 1fr 1fr 2fr',
        gap: '0.5rem',
        alignItems: 'center',
        padding: '0.7rem 1rem',
        backgroundColor: selected ? 'rgba(31, 160, 104, 0.06)' : hasRules ? 'rgba(220,50,50,0.03)' : 'rgba(255,255,255,0.02)',
        border: `1px solid ${borderColor}`,
        borderRadius: '0.5rem',
        cursor: 'pointer',
        transition: 'all 0.15s',
      }}
    >
      <span style={{ fontFamily: 'monospace', fontSize: '0.72rem', color: '#888890', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
        {tx.hash}
      </span>
      <span style={{ fontFamily: 'monospace', fontSize: '0.78rem', color: '#e4e4ec' }}>
        {tx.amount.toLocaleString()}
      </span>
      <span style={{ fontFamily: 'monospace', fontSize: '0.72rem', color: '#888890' }}>
        {tx.currency}
      </span>
      <RiskBar score={tx.riskScore} scanned={scanned} />
      <div style={{ display: 'flex', gap: '0.3rem', flexWrap: 'wrap' }}>
        {tx.rules.length > 0
          ? tx.rules.map(r => {
              const meta = RULE_META[r.code] || { color: '#888890', bg: 'rgba(136,136,144,0.1)' }
              return (
                <span key={r.code} style={{
                  fontFamily: 'monospace',
                  fontSize: '0.58rem',
                  padding: '0.15rem 0.4rem',
                  borderRadius: '0.2rem',
                  backgroundColor: meta.bg,
                  color: meta.color,
                  whiteSpace: 'nowrap',
                }}>
                  {r.code}
                </span>
              )
            })
          : scanned
          ? <span style={{ fontFamily: 'monospace', fontSize: '0.65rem', color: '#1fa068' }}>clean</span>
          : null
        }
      </div>
    </div>
  )
}
```

---

### `src/modules/AMLMonitor/RulePanel.tsx`

Create this new file:

```tsx
import { Transaction, RULE_META } from '../../data/aml-sample-transactions'

interface Props {
  tx: Transaction
  onClose: () => void
}

const SEVERITY_LABEL: Record<string, string> = {
  high: 'HIGH',
  medium: 'MEDIUM',
  low: 'LOW',
}

const SEVERITY_COLOR: Record<string, string> = {
  high: '#e55',
  medium: '#eab308',
  low: '#888890',
}

export default function RulePanel({ tx, onClose }: Props) {
  return (
    <div style={{
      width: '320px',
      flexShrink: 0,
      backgroundColor: '#0e0e12',
      border: '1px solid rgba(31, 160, 104, 0.18)',
      borderRadius: '0.75rem',
      display: 'flex',
      flexDirection: 'column',
      overflowY: 'auto',
    }}>
      {/* Panel header */}
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        padding: '1rem 1.25rem',
        borderBottom: '1px solid rgba(31, 160, 104, 0.1)',
      }}>
        <span style={{ fontFamily: 'monospace', fontSize: '0.65rem', textTransform: 'uppercase', letterSpacing: '0.1em', color: '#888890' }}>
          Rule Detail
        </span>
        <button
          onClick={onClose}
          style={{ background: 'none', border: 'none', color: '#555560', cursor: 'pointer', fontSize: '1rem', padding: '0 0.25rem' }}
        >
          ×
        </button>
      </div>

      {/* Transaction summary */}
      <div style={{ padding: '1rem 1.25rem', borderBottom: '1px solid rgba(31, 160, 104, 0.08)' }}>
        <div style={{ fontFamily: 'monospace', fontSize: '0.65rem', color: '#888890', marginBottom: '0.4rem' }}>{tx.hash}</div>
        <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
          <div>
            <div style={{ fontFamily: 'monospace', fontSize: '0.58rem', color: '#555560', textTransform: 'uppercase', letterSpacing: '0.08em' }}>Amount</div>
            <div style={{ fontFamily: 'monospace', fontSize: '0.9rem', color: '#e4e4ec', fontWeight: 600 }}>
              {tx.amount.toLocaleString()} {tx.currency}
            </div>
          </div>
          <div>
            <div style={{ fontFamily: 'monospace', fontSize: '0.58rem', color: '#555560', textTransform: 'uppercase', letterSpacing: '0.08em' }}>Risk Score</div>
            <div style={{ fontFamily: 'monospace', fontSize: '0.9rem', fontWeight: 700, color: tx.riskScore >= 70 ? '#e55' : tx.riskScore >= 40 ? '#eab308' : '#1fa068' }}>
              {tx.riskScore} / 100
            </div>
          </div>
        </div>
        <div style={{ fontFamily: 'monospace', fontSize: '0.62rem', color: '#555560', marginTop: '0.5rem' }}>
          {tx.timestamp}
        </div>
      </div>

      {/* Rules */}
      <div style={{ padding: '1rem 1.25rem', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
        {tx.rules.length === 0 ? (
          <div style={{ fontFamily: 'monospace', fontSize: '0.75rem', color: '#1fa068', textAlign: 'center', padding: '1.5rem 0' }}>
            No rules triggered. Transaction is clean.
          </div>
        ) : (
          tx.rules.map(rule => {
            const meta = RULE_META[rule.code] || { color: '#888890', bg: 'rgba(136,136,144,0.1)' }
            return (
              <div key={rule.code} style={{
                backgroundColor: meta.bg,
                border: `1px solid ${meta.color}30`,
                borderRadius: '0.5rem',
                padding: '0.9rem',
              }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                  <span style={{ fontFamily: 'monospace', fontSize: '0.72rem', fontWeight: 600, color: meta.color }}>
                    {rule.label}
                  </span>
                  <span style={{
                    fontFamily: 'monospace',
                    fontSize: '0.58rem',
                    padding: '0.15rem 0.4rem',
                    borderRadius: '0.2rem',
                    backgroundColor: `${SEVERITY_COLOR[rule.severity]}20`,
                    color: SEVERITY_COLOR[rule.severity],
                  }}>
                    {SEVERITY_LABEL[rule.severity]}
                  </span>
                </div>
                <p style={{ fontFamily: 'monospace', fontSize: '0.68rem', color: '#aaaabc', lineHeight: 1.55, margin: 0 }}>
                  {rule.explanation}
                </p>
              </div>
            )
          })
        )}
      </div>

      {/* Addresses */}
      <div style={{ padding: '0 1.25rem 1.25rem' }}>
        <div style={{ borderTop: '1px solid rgba(31,160,104,0.08)', paddingTop: '0.75rem' }}>
          {[
            { label: 'From', value: tx.from },
            { label: 'To', value: tx.to },
          ].map(({ label, value }) => (
            <div key={label} style={{ marginBottom: '0.5rem' }}>
              <div style={{ fontFamily: 'monospace', fontSize: '0.58rem', color: '#555560', textTransform: 'uppercase', letterSpacing: '0.08em' }}>{label}</div>
              <div style={{ fontFamily: 'monospace', fontSize: '0.65rem', color: '#888890', wordBreak: 'break-all' }}>{value}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
```

---

## Step 1: Create / Replace Files

- Replace `src/modules/AMLMonitor/index.tsx`
- Create `src/modules/AMLMonitor/TransactionRow.tsx`
- Create `src/modules/AMLMonitor/RulePanel.tsx`
- Create `src/data/aml-sample-transactions.ts`

---

## Step 2: Build and Deploy

```bash
npm run build
```

Push to GitHub — Cloudflare Pages auto-deploys.

---

## Step 3: Verify

- Navigate to `/aml-monitor`
- Counter bar shows: 15 transactions, rules/flagged/clean all showing `--`
- Click "Run Scan" — rows update one by one from top to bottom over ~2 seconds
- Flagged rows show red-tinted border and rule tags after scan
- Clean rows show green `clean` label
- Click any row — side panel slides in with rule details and explanations
- Click `×` on panel or same row — panel closes
- "Re-Scan" button resets and reruns
- Mobile at 375px: side panel stacks below the transaction list

---

## What Comes Next

Turn 004: Signal Intelligence — live BTC price from CoinGecko, heartbeat.json prediction history, sparkline chart.
