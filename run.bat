@echo off
REM Smart Fridge Recipe Generator - Quick Start Script for Windows

echo 🍳 Smart Fridge Recipe Generator
echo ================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/upgrade dependencies
echo 📥 Installing dependencies...
pip install -q --upgrade pip
pip install -q -r requirements.txt

REM Check for API key
if "%OPENAI_API_KEY%"=="" (
    echo.
    echo ⚠️  Warning: OPENAI_API_KEY environment variable not set
    echo You can either:
    echo   1. Set it now: set OPENAI_API_KEY=your-key-here
    echo   2. Enter it in the app's sidebar when it starts
    echo.
    pause
)

REM Run the app
echo.
echo 🚀 Starting the application...
echo The app will open in your browser at http://localhost:8501
echo.
streamlit run app.py

