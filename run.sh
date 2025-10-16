#!/bin/bash

# Smart Fridge Recipe Generator - Quick Start Script

echo "🍳 Smart Fridge Recipe Generator"
echo "================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install/upgrade dependencies
echo "📥 Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

# Check for API key
if [ -z "$OPENAI_API_KEY" ]; then
    echo ""
    echo "⚠️  Warning: OPENAI_API_KEY environment variable not set"
    echo "You can either:"
    echo "  1. Set it now: export OPENAI_API_KEY='your-key-here'"
    echo "  2. Enter it in the app's sidebar when it starts"
    echo ""
    read -p "Press Enter to continue..."
fi

# Run the app
echo ""
echo "🚀 Starting the application..."
echo "The app will open in your browser at http://localhost:8501"
echo ""
streamlit run app.py

