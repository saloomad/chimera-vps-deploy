param(
    [string]$Platform = "opencode"
)

$coordinationRepo = "C:\Users\becke\claudecowork\chimera-vps-deploy"
$guardScript = Join-Path $coordinationRepo "scripts\github_coordination_guard.py"

if (-not (Test-Path $guardScript)) {
    throw "Missing guard script at $guardScript"
}

python $guardScript validate-platform --coordination-root $coordinationRepo --platform $Platform
