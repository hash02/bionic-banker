# AML Proof Public Page

Date: 2026-05-24 UTC

## Scope

Created a visible Bionic Banker public proof page for the AML Layer 1 evidence contract without exposing private machine paths, secrets, employer data, client data, account-level details, or operational authority.

## Files changed

Source:

- `_astro-source/src/pages/aml-proof.astro`
- `_astro-source/public/dashboard-data/aml-proof-public.json`
- `_astro-source/src/layouts/BaseLayout.astro`
- `_astro-source/src/pages/projects.astro`
- `_astro-source/src/pages/proof-tour.astro`
- `_astro-source/scripts/check-aml-proof-page.mjs`
- `_astro-source/package.json`

Built/public output:

- `aml-proof/index.html`
- `dashboard-data/aml-proof-public.json`
- rebuilt static pages and sitemap generated from Astro build output

## Public route

- Local/static route: `/aml-proof/`
- Page title: `AML Proof - Bionic Banker`
- Navigation/footer/mobile menu now expose `AML Proof`
- Experiments and Proof Tour link into the page

## Boundary preserved

The public page states:

- `may_execute: false`
- No wallet, trade, filing, or deploy authority
- No KYC approval authority
- Proof surface only, not an operational compliance product

The page uses repository-relative provenance only. It does not publish local Windows paths or private infrastructure details.

## Verification

Commands run:

```bash
npm run test:aml-proof
npm run build
cp -a dist/. ..
test -f ../aml-proof/index.html && grep -q 'may_execute: false' ../aml-proof/index.html
```

Results:

- `npm run test:aml-proof` passed
- `npm run build` passed, building 58 static pages including `/aml-proof/index.html`
- Root static output smoke check passed
- Browser check at `http://127.0.0.1:4177/aml-proof/` loaded with title `AML Proof - Bionic Banker`
- Visual inspection confirmed the desktop layout is coherent and the authority card is not clipped

## Notes

A canonical latest AML evidence artifact was not present in `70-ops-logs/aml-evidence/` during this pass, so the public page does not claim a live artifact body. It publishes the evidence contract, artifact pattern, receipt trail, and authority boundary instead.
