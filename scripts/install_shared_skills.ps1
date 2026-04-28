param(
    [string]$RepoRoot = "C:\Users\becke\claudecowork\chimera-vps-deploy",
    [string]$TargetSkillsHome = "C:\Users\becke\.codex\skills"
)

$skillNames = @(
    "codex-runtime-router",
    "model-registry",
    "github-manager",
    "project-operations-manager",
    "agent-session-resume",
    "openclaw-replay-and-backtest",
    "strategy-backtest-lab",
    "pipeline-simulation-lab",
    "openclaw-workspace"
)

New-Item -ItemType Directory -Force -Path $TargetSkillsHome | Out-Null

foreach ($name in $skillNames) {
    $source = Join-Path $RepoRoot "skills\\$name"
    if (Test-Path $source) {
        Copy-Item -Path $source -Destination $TargetSkillsHome -Recurse -Force
        Write-Output "Installed $name"
    }
}
