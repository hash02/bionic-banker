param(
  [Parameter(Mandatory = $true)]
  [string]$Brief,

  [Parameter(Mandatory = $true)]
  [string]$Slug,

  [string]$OutputRoot = "blog-visuals",
  [string]$Remote = $env:BB_CAROUSEL_REMOTE,
  [string]$SshKey = $env:BB_CAROUSEL_SSH_KEY,
  [string]$RemoteOutputRoot = "~/carousel-output",

  [switch]$Commit,
  [switch]$ValidateOnly
)

$ErrorActionPreference = "Stop"

function Stop-Factory {
  param([string]$Message)
  throw "[carousel-factory] $Message"
}

function Require-Tool {
  param([string]$Name)
  if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
    Stop-Factory "missing required command: $Name"
  }
}

function Assert-SafeSlug {
  param([string]$Value)
  if ($Value -notmatch "^[a-z0-9][a-z0-9-]{1,80}$") {
    Stop-Factory "slug must be lowercase letters, numbers, and hyphens only"
  }
}

Require-Tool git
Require-Tool ssh
Require-Tool scp
Require-Tool python
Assert-SafeSlug $Slug

$repoRoot = (Resolve-Path -LiteralPath ".").Path
$briefPath = (Resolve-Path -LiteralPath $Brief).Path
$briefData = Get-Content -Raw -LiteralPath $briefPath | ConvertFrom-Json

$hasSlides = $null -ne $briefData.slides
if ((-not $hasSlides) -or ($briefData.slides.Count -lt 1)) {
  Stop-Factory "brief needs a non-empty slides array"
}

$width = [int]$briefData.dimensions.width
$height = [int]$briefData.dimensions.height
if ($width -ne 1080 -or $height -ne 1080) {
  Stop-Factory "brief dimensions must be 1080x1080"
}

$slideCount = [int]$briefData.slides.Count
$expectedPdfName = "$Slug.pdf"
$relativeOutput = Join-Path $OutputRoot $Slug
$outputDir = Join-Path $repoRoot $relativeOutput
$fullOutputDir = [System.IO.Path]::GetFullPath($outputDir)

if (-not $fullOutputDir.StartsWith($repoRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
  Stop-Factory "output directory resolved outside repo"
}

if ([string]::IsNullOrWhiteSpace($Remote)) {
  Stop-Factory "set BB_CAROUSEL_REMOTE or pass -Remote"
}

if ([string]::IsNullOrWhiteSpace($SshKey)) {
  Stop-Factory "set BB_CAROUSEL_SSH_KEY or pass -SshKey"
}

if (-not (Test-Path -LiteralPath $SshKey)) {
  Stop-Factory "SSH key was not found"
}

$remoteBrief = "/tmp/$Slug.json"
$remoteDir = "$RemoteOutputRoot/$Slug"
$renderCommand = "python3 ~/maya01-brain/tools/build_carousel.py --slug '$Slug' --brief '$remoteBrief' --output '$RemoteOutputRoot'"

Write-Host "[carousel-factory] brief: $briefPath"
Write-Host "[carousel-factory] slug: $Slug"
Write-Host "[carousel-factory] slides: $slideCount"
Write-Host "[carousel-factory] output: $relativeOutput"

if ($ValidateOnly) {
  Write-Host "[carousel-factory] validate-only passed"
  Write-Host "[carousel-factory] remote render command: $renderCommand"
  exit 0
}

& ssh -i $SshKey -o BatchMode=yes $Remote "test -f ~/maya01-brain/tools/build_carousel.py"
if ($LASTEXITCODE -ne 0) {
  Stop-Factory "remote carousel builder not found"
}

if (Test-Path -LiteralPath $fullOutputDir) {
  Remove-Item -LiteralPath $fullOutputDir -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $fullOutputDir | Out-Null

& scp -i $SshKey $briefPath "${Remote}:$remoteBrief"
if ($LASTEXITCODE -ne 0) {
  Stop-Factory "failed to upload brief"
}

& ssh -i $SshKey -o BatchMode=yes $Remote $renderCommand
if ($LASTEXITCODE -ne 0) {
  Stop-Factory "remote render failed"
}

& scp -i $SshKey "${Remote}:$remoteDir/slide-*.png" $fullOutputDir
if ($LASTEXITCODE -ne 0) {
  Stop-Factory "failed to pull slide PNGs"
}

& scp -i $SshKey "${Remote}:$remoteDir/$expectedPdfName" $fullOutputDir
if ($LASTEXITCODE -ne 0) {
  Stop-Factory "failed to pull PDF"
}

$verifyScript = @"
from pathlib import Path
from PIL import Image
import sys

out = Path(r'''$fullOutputDir''')
slug = '''$Slug'''
expected = $slideCount
slides = sorted(out.glob('slide-*.png'))
if len(slides) != expected:
    raise SystemExit(f'expected {expected} slides, found {len(slides)}')
for slide in slides:
    with Image.open(slide) as img:
        if img.size != (1080, 1080):
            raise SystemExit(f'{slide.name} is {img.size}, expected 1080x1080')
pdf = out / f'{slug}.pdf'
if not pdf.exists():
    raise SystemExit('missing PDF')
if pdf.stat().st_size < 10_000:
    raise SystemExit('PDF looks too small')
print(f'verified {len(slides)} slides and {pdf.name} ({pdf.stat().st_size} bytes)')
"@

$verifyScript | python
if ($LASTEXITCODE -ne 0) {
  Stop-Factory "local output verification failed"
}

if ($Commit) {
  & git pull --rebase origin main
  if ($LASTEXITCODE -ne 0) {
    Stop-Factory "git pull failed"
  }

  & git add -- $relativeOutput
  if ($LASTEXITCODE -ne 0) {
    Stop-Factory "git add failed"
  }

  & git commit -m "content: add $Slug carousel assets"
  if ($LASTEXITCODE -ne 0) {
    Stop-Factory "git commit failed"
  }

  & git push origin main
  if ($LASTEXITCODE -ne 0) {
    Stop-Factory "git push failed"
  }
}

Write-Host "[carousel-factory] ready: $relativeOutput"
