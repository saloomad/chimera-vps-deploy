$configPath = "C:\Users\becke\.codex\config.toml"
$model = "unknown"
$reasoning = "unknown"

if (Test-Path $configPath) {
    $config = Get-Content $configPath
    foreach ($line in $config) {
        if ($line -match '^model = "(.+)"$') { $model = $Matches[1] }
        if ($line -match '^model_reasoning_effort = "(.+)"$') { $reasoning = $Matches[1] }
    }
}

$quota = "not exposed"
$usageProbe = @()
$codexPath = (Get-Command codex -ErrorAction SilentlyContinue)
$commands = @(
    "codex login status",
    "codex usage",
    "codex quota",
    "codex account"
)

if (-not $codexPath) {
    $usageProbe += [pscustomobject]@{
        command = "codex"
        output = "CLI not found on PATH"
    }
} else {
    foreach ($cmd in $commands) {
        try {
            $output = Invoke-Expression $cmd 2>&1 | Out-String
            $trimmed = $output.Trim()
            if (-not $trimmed) {
                $trimmed = "no output"
            }
            $usageProbe += [pscustomobject]@{
                command = $cmd
                output = $trimmed
            }
            if ($trimmed -match 'quota|remaining|used|limit') {
                $quota = "check-output"
            }
        } catch {
            $usageProbe += [pscustomobject]@{
                command = $cmd
                output = $_.Exception.Message
            }
        }
    }
}

[pscustomobject]@{
    model = $model
    reasoning = $reasoning
    quota = $quota
    codex_path = if ($codexPath) { $codexPath.Source } else { "not found" }
    probes = $usageProbe
} | ConvertTo-Json -Depth 4
