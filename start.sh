#!/bin/bash

echo "========================================"
echo "   📰 CHRONOS NEWS AGGREGATOR"
echo "========================================"
echo ""

echo "🔧 Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python is not installed!"
    echo "Please install Python 3.8 or higher"
    exit 1
fi
echo "✓ Python is installed"
python3 --version
echo ""

echo "📦 Installing required packages..."
pip3 install flask selenium
echo ""

echo "🚀 Starting Chronos News Aggregator..."
echo ""
echo "========================================"
echo "   Server is starting..."
echo "   Please wait while we gather the news"
echo "========================================"
echo ""

python3 app.py