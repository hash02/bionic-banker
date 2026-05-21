param(
  [string]$SourceOutput = "_astro-source/public/dashboard-data/context-signals.json",
  [string]$RootOutput = "dashboard-data/context-signals.json"
)

$ErrorActionPreference = "Stop"

function Stop-Context {
  param([string]$Message)
  throw "[context-signals] $Message"
}

function Read-OwidCsv {
  param([string]$Slug)
  $uri = "https://ourworldindata.org/grapher/$Slug.csv?csvType=full&useColumnShortNames=false"
  $response = Invoke-WebRequest -Uri $uri -UseBasicParsing
  return $response.Content | ConvertFrom-Csv
}

function Read-OwidMeta {
  param([string]$Slug)
  $uri = "https://ourworldindata.org/grapher/$Slug.metadata.json"
  return Invoke-RestMethod -Uri $uri
}

function World-Series {
  param(
    [object[]]$Rows,
    [string]$ColumnName
  )
  $series = $Rows |
    Where-Object { $_.Entity -eq "World" -and $_.$ColumnName -ne "" } |
    Sort-Object { [int]$_.Year } |
    ForEach-Object {
      [pscustomobject]@{
        year = [int]$_.Year
        value = [double]$_.$ColumnName
      }
    }

  if (-not $series -or $series.Count -lt 2) {
    Stop-Context "not enough World rows for $ColumnName"
  }

  $maxValue = ($series | Measure-Object -Property value -Maximum).Maximum
  return $series | ForEach-Object {
    [pscustomobject]@{
      year = $_.year
      value = $_.value
      pct = [math]::Round(($_.value / $maxValue) * 100, 1)
    }
  }
}

function Format-CompactNumber {
  param([double]$Value)
  if ($Value -ge 1000000000) {
    return "$([math]::Round($Value / 1000000000, 1))B"
  }
  if ($Value -ge 1000000) {
    return "$([math]::Round($Value / 1000000, 1))M"
  }
  if ($Value -ge 1000) {
    return "{0:n0}" -f $Value
  }
  return "$Value"
}

$aiSlug = "newly-funded-artificial-intelligence-companies"
$internetSlug = "share-of-individuals-using-the-internet"

$aiRows = Read-OwidCsv -Slug $aiSlug
$internetRows = Read-OwidCsv -Slug $internetSlug
$aiMeta = Read-OwidMeta -Slug $aiSlug
$internetMeta = Read-OwidMeta -Slug $internetSlug

$aiSeries = @(World-Series -Rows $aiRows -ColumnName "Newly founded AI companies")
$internetSeries = @(World-Series -Rows $internetRows -ColumnName "Share of the population using the Internet")

$aiLatest = $aiSeries[-1]
$aiFirst = $aiSeries[0]
$internetLatest = $internetSeries[-1]

$articleCount = @(Get-ChildItem -Path "_astro-source/src/content/blog" -Filter "*.md" -File).Count
$carouselCount = @(Get-ChildItem -Path "blog-visuals" -Directory -Filter "*carousel*" -ErrorAction SilentlyContinue).Count
$visualCount = @(Get-ChildItem -Path "blog-visuals" -Recurse -File -Include "*.png", "*.pdf" -ErrorAction SilentlyContinue).Count

$heartbeatPath = "dashboard-data/heartbeat.json"
$signalRows = $null
if (Test-Path -LiteralPath $heartbeatPath) {
  $hb = Get-Content -Raw -LiteralPath $heartbeatPath | ConvertFrom-Json
  $signalRows = $hb.status.predictions_made
}

$projectSeries = @(
  [pscustomobject]@{ year = 1; value = [double]$articleCount; pct = 100 },
  [pscustomobject]@{ year = 2; value = [double]$visualCount; pct = [math]::Min(100, [math]::Round(($visualCount / [math]::Max($articleCount, 1)) * 100, 1)) },
  [pscustomobject]@{ year = 3; value = [double]$carouselCount; pct = [math]::Min(100, [math]::Round(($carouselCount / [math]::Max($articleCount, 1)) * 100, 1)) }
)

$data = [ordered]@{
  generated_at = (Get-Date).ToUniversalTime().ToString("o")
  cards = @(
    [ordered]@{
      id = "ai-company-formation"
      label = "AI context"
      title = "AI company formation keeps moving"
      value = (Format-CompactNumber -Value $aiLatest.value)
      unit = "newly funded AI companies"
      detail = "Worldwide AI companies above the dataset funding threshold in $($aiLatest.year), up from $([int]$aiFirst.value) in $($aiFirst.year)."
      source = $aiMeta.chart.citation
      source_url = "https://ourworldindata.org/grapher/$aiSlug"
      series = @($aiSeries | Select-Object -Last 8)
    }
    [ordered]@{
      id = "internet-reach"
      label = "Reach"
      title = "The audience is already online"
      value = "$([math]::Round($internetLatest.value, 1))%"
      unit = "of the world"
      detail = "Share of the world population using the internet in $($internetLatest.year). This is why small public labs can travel."
      source = $internetMeta.chart.citation
      source_url = "https://ourworldindata.org/grapher/$internetSlug"
      series = @($internetSeries | Select-Object -Last 8)
    }
    [ordered]@{
      id = "bionic-visual-layer"
      label = "Bionic Banker"
      title = "The text layer is becoming visual"
      value = "$visualCount"
      unit = "visual assets"
      detail = "$articleCount articles, $carouselCount carousel packs, and $(if ($signalRows) { $signalRows } else { 'live' }) signal rows give the site more than text to point at."
      source = "Bionic Banker repo snapshot"
      source_url = "/reports"
      series = $projectSeries
    }
  )
  sources = @(
    [ordered]@{
      name = "Our World in Data Grapher Chart API"
      url = "https://docs.owid.io/projects/etl/api/chart-api/"
      note = "Chart data is fetched from public CSV endpoints with chart metadata for citation."
    }
    [ordered]@{
      name = "Our World in Data reuse guidance"
      url = "https://ourworldindata.org/faqs"
      note = "Public reuse needs attribution and cannot imply endorsement."
    }
  )
}

$json = $data | ConvertTo-Json -Depth 10

foreach ($path in @($SourceOutput, $RootOutput)) {
  $dir = Split-Path -Parent $path
  if ($dir -and -not (Test-Path -LiteralPath $dir)) {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
  }
  $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
  [System.IO.File]::WriteAllText((Resolve-Path -LiteralPath $dir).Path + [System.IO.Path]::DirectorySeparatorChar + (Split-Path -Leaf $path), $json + [Environment]::NewLine, $utf8NoBom)
}

Write-Host "[context-signals] wrote $SourceOutput and $RootOutput"
