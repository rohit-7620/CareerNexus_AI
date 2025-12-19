# AI Career Advisor - Startup Script
# This script starts the Flask application

Write-Host ""
Write-Host "="*70 -ForegroundColor Cyan
Write-Host "Starting AI Career Advisor - Hackathon Edition" -ForegroundColor Green
Write-Host "="*70 -ForegroundColor Cyan
Write-Host ""

# Activate virtual environment
$venvPath = ".\.venv\Scripts\Activate.ps1"
if (Test-Path $venvPath) {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & $venvPath
} else {
    Write-Host "Virtual environment not found. Please run setup first." -ForegroundColor Red
    exit 1
}

# Start the application
Write-Host "Starting Flask server..." -ForegroundColor Yellow
Write-Host ""

python app.py
