#!/bin/bash
# AI Career Advisor - Startup Script (Linux/Mac)

echo ""
echo "======================================================================"
echo "Starting AI Career Advisor - Hackathon Edition"
echo "======================================================================"
echo ""

# Activate virtual environment
if [ -d ".venv" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
else
    echo "Virtual environment not found. Please run setup first."
    exit 1
fi

# Start the application
echo "Starting Flask server..."
echo ""

python app.py
