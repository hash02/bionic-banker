param(
  [string[]]$Paths = @(
    "_astro-source\src\pages\gaps.astro",
    "_astro-source\src\pages\intelligence.astro",
    "_astro-source\src\pages\learn.astro",
    "_astro-source\src\pages\proof-tour.astro",
    "_astro-source\src\pages\projects.astro",
    "_astro-source\src\pages\portfolio.astro",
    "_astro-source\src\pages\investigate.astro",
    "_astro-source\src\pages\reports.astro",
    "_astro-source\src\pages\site-agent.astro",
    "_astro-source\public\dashboard-data\market-gap-catalog.json",
    "_astro-source\public\dashboard-data\intelligence-signal-catalog.json",
    "_astro-source\public\dashboard-data\public-proof-catalog.json",
    "_astro-source\public\dashboard-data\engineering-report-catalog.json",
    "gaps\index.html",
    "intelligence\index.html",
    "learn\index.html",
    "proof-tour\index.html",
    "projects\index.html",
    "portfolio\index.html",
    "investigate\index.html",
    "reports\index.html",
    "site-agent\index.html"
  )
)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$checks = @(
  @{ Phrase = "public-safe"; Suggestion = "Use reader-facing, source-linked, visible, inspectable, or privacy-aware." },
  @{ Phrase = "safe to show"; Suggestion = "Use visible or inspectable." },
  @{ Phrase = "allowed to show"; Suggestion = "Use what readers can inspect." },
  @{ Phrase = "not asking the reader"; Suggestion = "Lead with what the reader can do." },
  @{ Phrase = "believe a roadmap"; Suggestion = "Point to examples that already exist." },
  @{ Phrase = "what we are building"; Suggestion = "Use what exists or how this works." },
  @{ Phrase = "we are building"; Suggestion = "Use what exists or how this works." },
  @{ Phrase = "proof to build next"; Suggestion = "Use next question." },
  @{ Phrase = "next build"; Suggestion = "Use next question." },
  @{ Phrase = "strongest next demo"; Suggestion = "Use strongest next question." },
  @{ Phrase = "private infrastructure"; Suggestion = "Use backend details or operational details." },
  @{ Phrase = "private operations"; Suggestion = "Use operational details only when needed." },
  @{ Phrase = "internal roadmap"; Suggestion = "Use future direction or omit." },
  @{ Phrase = "Rows the system can safely show"; Suggestion = "Use Visible signal rows." }
)

$findings = New-Object System.Collections.Generic.List[object]

foreach ($relativePath in $Paths) {
  $path = Join-Path $root $relativePath
  if (-not (Test-Path -LiteralPath $path)) {
    continue
  }

  $lines = @(Get-Content -LiteralPath $path)
  for ($i = 0; $i -lt $lines.Count; $i++) {
    foreach ($check in $checks) {
      if ($lines[$i].IndexOf($check.Phrase, [System.StringComparison]::OrdinalIgnoreCase) -ge 0) {
        $findings.Add([pscustomobject]@{
          Path = $relativePath
          Line = $i + 1
          Phrase = $check.Phrase
          Suggestion = $check.Suggestion
        })
      }
    }
  }
}

if ($findings.Count -gt 0) {
  Write-Host "Bionic Banker editor check found public copy issues:" -ForegroundColor Yellow
  foreach ($finding in $findings) {
    Write-Host ("{0}:{1}: {2} -> {3}" -f $finding.Path, $finding.Line, $finding.Phrase, $finding.Suggestion)
  }
  exit 1
}

Write-Host "Bionic Banker editor check passed."
