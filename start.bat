@echo off
title Chronos News Aggregator
color 0A

echo.
echo ========================================
echo    📰 CHRONOS NEWS AGGREGATOR
echo ========================================
echo.

echo 🔧 Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed!
    echo Please install Python 3.8 or higher from https://python.org
    pause
    exit /b 1
)
echo ✓ Python is installed
python --version
echo.

echo 📦 Installing required packages...
pip install flask selenium
echo.

echo 🚀 Starting Chronos News Aggregator...
echo.
echo ========================================
echo    Server is starting...
echo    Please wait while we gather the news
echo ========================================
echo.

python app.py

pause