$uv = "$HOME\.local\bin\uv.exe"

Write-Host "Running tests..." -ForegroundColor Cyan
& $uv run pytest -q

if ($LASTEXITCODE -ne 0) {
    Write-Host "Tests failed" -ForegroundColor Red
    exit 1
}

Write-Host "Running lint..." -ForegroundColor Cyan
& $uv run ruff check .

if ($LASTEXITCODE -ne 0) {
    Write-Host "Lint failed" -ForegroundColor Red
    exit 1
}

Write-Host "All checks passed!" -ForegroundColor Green