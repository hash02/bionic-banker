# Codex Bionic Lab — Turn 001: App Scaffold

Date: 2026-05-20
Actor: Codex
Written by: Claude

---

## What This Turn Does

Scaffolds the `bionic-lab` React app from scratch using the files below. Claude has written all the code. Codex creates the files, installs dependencies, runs the build, and deploys to Cloudflare Pages.

No code decisions needed from Codex — just create the files exactly as written and run the commands.

---

## Step 1: Create the Repo

```bash
# [WINDOWS or WUKONG — wherever Codex runs git]
mkdir bionic-lab
cd bionic-lab
git init
git branch -M main
```

Create a new GitHub repo `bionic-lab` under hash02, then:
```bash
git remote add origin https://github.com/hash02/bionic-lab.git
```

---

## Step 2: Create All Files

Create each file exactly as written below. No modifications.

---

### `package.json`

```json
{
  "name": "bionic-lab",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^6.23.1",
    "recharts": "^2.12.7"
  },
  "devDependencies": {
    "@types/react": "^18.3.3",
    "@types/react-dom": "^18.3.0",
    "@vitejs/plugin-react": "^4.3.1",
    "autoprefixer": "^10.4.19",
    "postcss": "^8.4.38",
    "tailwindcss": "^3.4.4",
    "typescript": "^5.4.5",
    "vite": "^5.3.1"
  }
}
```

---

### `vite.config.ts`

```ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
})
```

---

### `tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

---

### `tsconfig.node.json`

```json
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true
  },
  "include": ["vite.config.ts", "tailwind.config.ts"]
}
```

---

### `tailwind.config.ts`

```ts
import type { Config } from 'tailwindcss'

export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        bg: '#08080e',
        surface: '#0e0e12',
        accent: '#1fa068',
        primary: '#e4e4ec',
        muted: '#888890',
      },
      fontFamily: {
        mono: ['"SF Mono"', '"Fira Code"', 'monospace'],
        sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
} satisfies Config
```

---

### `postcss.config.js`

```js
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

---

### `index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Bionic Lab</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

---

### `public/_redirects`

```
/*  /index.html  200
```

This file handles SPA routing on Cloudflare Pages so direct URL visits to `/aml-monitor` etc. work.

---

### `src/index.css`

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  html,
  body,
  #root {
    height: 100%;
    background-color: #08080e;
    color: #e4e4ec;
  }

  * {
    box-sizing: border-box;
  }

  ::-webkit-scrollbar {
    width: 4px;
  }
  ::-webkit-scrollbar-track {
    background: #08080e;
  }
  ::-webkit-scrollbar-thumb {
    background: rgba(31, 160, 104, 0.2);
    border-radius: 2px;
  }
  ::-webkit-scrollbar-thumb:hover {
    background: rgba(31, 160, 104, 0.4);
  }
}
```

---

### `src/main.tsx`

```tsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```

---

### `src/App.tsx`

```tsx
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Sidebar from './components/Sidebar'
import TopBar from './components/TopBar'
import FinancialPlanning from './modules/FinancialPlanning'
import AMLMonitor from './modules/AMLMonitor'
import SignalIntelligence from './modules/SignalIntelligence'
import MarketPulse from './modules/MarketPulse'
import AgentStatus from './modules/AgentStatus'

export default function App() {
  return (
    <BrowserRouter>
      <div style={{ display: 'flex', height: '100vh', backgroundColor: '#08080e', color: '#e4e4ec', overflow: 'hidden' }}>
        <Sidebar />
        <div style={{ display: 'flex', flexDirection: 'column', flex: 1, minWidth: 0 }}>
          <TopBar />
          <main style={{ flex: 1, overflowY: 'auto', padding: '1.5rem' }}>
            <Routes>
              <Route path="/" element={<Navigate to="/financial-planning" replace />} />
              <Route path="/financial-planning" element={<FinancialPlanning />} />
              <Route path="/aml-monitor" element={<AMLMonitor />} />
              <Route path="/signal-intelligence" element={<SignalIntelligence />} />
              <Route path="/market-pulse" element={<MarketPulse />} />
              <Route path="/agent-status" element={<AgentStatus />} />
            </Routes>
          </main>
        </div>
      </div>
    </BrowserRouter>
  )
}
```

---

### `src/components/Sidebar.tsx`

```tsx
import { NavLink } from 'react-router-dom'

const nav = [
  { to: '/financial-planning', label: 'Financial Planning', icon: '◈' },
  { to: '/aml-monitor', label: 'AML Monitor', icon: '⊕' },
  { to: '/signal-intelligence', label: 'Signal Intelligence', icon: '◉' },
  { to: '/market-pulse', label: 'Market Pulse', icon: '◈' },
  { to: '/agent-status', label: 'Agent Status', icon: '⊙' },
]

export default function Sidebar() {
  return (
    <aside style={{
      width: '220px',
      flexShrink: 0,
      backgroundColor: '#0e0e12',
      borderRight: '1px solid rgba(31, 160, 104, 0.12)',
      display: 'flex',
      flexDirection: 'column',
    }}>
      <div style={{
        padding: '1.25rem 1rem',
        borderBottom: '1px solid rgba(31, 160, 104, 0.12)',
      }}>
        <div style={{ fontFamily: 'monospace', fontSize: '0.65rem', color: '#888890', textTransform: 'uppercase', letterSpacing: '0.12em' }}>
          Bionic Lab
        </div>
        <div style={{ marginTop: '0.4rem', width: '1.5rem', height: '2px', backgroundColor: '#1fa068', borderRadius: '1px' }} />
      </div>

      <nav style={{ flex: 1, padding: '0.75rem 0' }}>
        {nav.map(({ to, label, icon }) => (
          <NavLink
            key={to}
            to={to}
            style={({ isActive }) => ({
              display: 'flex',
              alignItems: 'center',
              gap: '0.6rem',
              padding: '0.6rem 1rem',
              fontFamily: 'monospace',
              fontSize: '0.78rem',
              textDecoration: 'none',
              transition: 'all 0.15s',
              color: isActive ? '#1fa068' : '#888890',
              backgroundColor: isActive ? 'rgba(31, 160, 104, 0.08)' : 'transparent',
              borderRight: isActive ? '2px solid #1fa068' : '2px solid transparent',
            })}
          >
            <span style={{ fontSize: '0.7rem' }}>{icon}</span>
            {label}
          </NavLink>
        ))}
      </nav>

      <div style={{
        padding: '1rem',
        borderTop: '1px solid rgba(31, 160, 104, 0.12)',
      }}>
        <a
          href="https://bionicbanker.tech"
          target="_blank"
          rel="noopener noreferrer"
          style={{ fontFamily: 'monospace', fontSize: '0.65rem', color: '#888890', textDecoration: 'none' }}
        >
          ← bionicbanker.tech
        </a>
      </div>
    </aside>
  )
}
```

---

### `src/components/TopBar.tsx`

```tsx
import { useLocation } from 'react-router-dom'

const titles: Record<string, string> = {
  '/financial-planning': 'Financial Planning',
  '/aml-monitor': 'AML Monitor',
  '/signal-intelligence': 'Signal Intelligence',
  '/market-pulse': 'Market Pulse',
  '/agent-status': 'Agent Status',
}

export default function TopBar() {
  const { pathname } = useLocation()
  const title = titles[pathname] || 'Bionic Lab'

  return (
    <header style={{
      height: '3.5rem',
      display: 'flex',
      alignItems: 'center',
      padding: '0 1.5rem',
      borderBottom: '1px solid rgba(31, 160, 104, 0.12)',
      backgroundColor: 'rgba(14, 14, 18, 0.8)',
      backdropFilter: 'blur(8px)',
      flexShrink: 0,
    }}>
      <h1 style={{ fontFamily: 'monospace', fontSize: '0.82rem', fontWeight: 600, color: '#e4e4ec', letterSpacing: '0.04em', margin: 0 }}>
        {title}
      </h1>
      <div style={{ marginLeft: 'auto', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
        <span style={{ fontFamily: 'monospace', fontSize: '0.65rem', color: '#1fa068', display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
          <span style={{
            width: '6px', height: '6px', borderRadius: '50%', backgroundColor: '#1fa068',
            animation: 'pulse 2s infinite',
          }} />
          LIVE
        </span>
      </div>
    </header>
  )
}
```

---

### `src/components/ui/Card.tsx`

```tsx
import { ReactNode } from 'react'

interface CardProps {
  children: ReactNode
  style?: React.CSSProperties
}

export default function Card({ children, style }: CardProps) {
  return (
    <div style={{
      backgroundColor: '#0e0e12',
      border: '1px solid rgba(31, 160, 104, 0.15)',
      borderRadius: '0.75rem',
      padding: '1.25rem',
      ...style,
    }}>
      {children}
    </div>
  )
}
```

---

### `src/components/ui/Badge.tsx`

```tsx
interface BadgeProps {
  label: string
  variant?: 'default' | 'accent' | 'muted' | 'warn'
}

const styles: Record<string, React.CSSProperties> = {
  default: { backgroundColor: 'rgba(31, 160, 104, 0.12)', color: '#1fa068' },
  accent: { backgroundColor: '#1fa068', color: '#08080e' },
  muted: { backgroundColor: 'rgba(255,255,255,0.05)', color: '#888890' },
  warn: { backgroundColor: 'rgba(234, 179, 8, 0.1)', color: '#eab308' },
}

export default function Badge({ label, variant = 'default' }: BadgeProps) {
  return (
    <span style={{
      fontFamily: 'monospace',
      fontSize: '0.65rem',
      padding: '0.2rem 0.5rem',
      borderRadius: '0.25rem',
      ...styles[variant],
    }}>
      {label}
    </span>
  )
}
```

---

### `src/components/ui/MetricTile.tsx`

```tsx
interface MetricTileProps {
  label: string
  value: string
  sub?: string
  accent?: boolean
}

export default function MetricTile({ label, value, sub, accent }: MetricTileProps) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '0.2rem' }}>
      <span style={{ fontFamily: 'monospace', fontSize: '0.6rem', textTransform: 'uppercase', letterSpacing: '0.1em', color: '#888890' }}>
        {label}
      </span>
      <strong style={{ fontFamily: 'monospace', fontSize: '1.4rem', fontWeight: 700, color: accent ? '#1fa068' : '#e4e4ec', lineHeight: 1.1 }}>
        {value}
      </strong>
      {sub && (
        <span style={{ fontFamily: 'monospace', fontSize: '0.62rem', color: '#888890' }}>
          {sub}
        </span>
      )}
    </div>
  )
}
```

---

### `src/modules/FinancialPlanning/index.tsx` (placeholder)

```tsx
export default function FinancialPlanning() {
  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      height: '16rem',
      border: '1px solid rgba(31, 160, 104, 0.15)',
      borderRadius: '0.75rem',
      color: '#888890',
      fontFamily: 'monospace',
      fontSize: '0.82rem',
    }}>
      Financial Planning — Turn B
    </div>
  )
}
```

---

### `src/modules/AMLMonitor/index.tsx` (placeholder)

```tsx
export default function AMLMonitor() {
  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      height: '16rem',
      border: '1px solid rgba(31, 160, 104, 0.15)',
      borderRadius: '0.75rem',
      color: '#888890',
      fontFamily: 'monospace',
      fontSize: '0.82rem',
    }}>
      AML Monitor — Turn C
    </div>
  )
}
```

---

### `src/modules/SignalIntelligence/index.tsx` (placeholder)

```tsx
export default function SignalIntelligence() {
  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      height: '16rem',
      border: '1px solid rgba(31, 160, 104, 0.15)',
      borderRadius: '0.75rem',
      color: '#888890',
      fontFamily: 'monospace',
      fontSize: '0.82rem',
    }}>
      Signal Intelligence — Turn D
    </div>
  )
}
```

---

### `src/modules/MarketPulse/index.tsx` (placeholder)

```tsx
export default function MarketPulse() {
  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      height: '16rem',
      border: '1px solid rgba(31, 160, 104, 0.15)',
      borderRadius: '0.75rem',
      color: '#888890',
      fontFamily: 'monospace',
      fontSize: '0.82rem',
    }}>
      Market Pulse — Turn E
    </div>
  )
}
```

---

### `src/modules/AgentStatus/index.tsx` (placeholder)

```tsx
export default function AgentStatus() {
  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      height: '16rem',
      border: '1px solid rgba(31, 160, 104, 0.15)',
      borderRadius: '0.75rem',
      color: '#888890',
      fontFamily: 'monospace',
      fontSize: '0.82rem',
    }}>
      Agent Status — Turn E
    </div>
  )
}
```

---

## Step 3: Install and Build

```bash
npm install
npm run build
```

Expected: `dist/` folder created, 0 errors.

If TypeScript errors appear from strict mode, add `// @ts-ignore` on the line above. Do not change the tsconfig.

---

## Step 4: Deploy to Cloudflare Pages

1. Go to Cloudflare Pages dashboard
2. Create new project → Connect to GitHub → select `bionic-lab`
3. Build settings:
   - Framework preset: None (Vite)
   - Build command: `npm run build`
   - Build output directory: `dist`
4. Deploy

Expected URL: something like `bionic-lab-xxx.pages.dev`

---

## Step 5: Verify

- App loads at the Cloudflare Pages URL
- Sidebar shows 5 nav items
- Clicking each nav item updates the page title in TopBar
- Each module shows the placeholder text
- No browser console errors
- Direct URL visit to `/aml-monitor` works (not 404) — this confirms `_redirects` is working

---

## What Comes Next

Turn 002: Claude writes the full Financial Planning module — projection math, 3-scenario Recharts AreaChart, slider inputs. Codex copies the module files and rebuilds.

---

## What NOT to Change

- Color values — use exactly what's written
- File structure — matches the plan exactly
- Placeholder text — it's intentional until each module turn
