@echo off
REM MarketAI Suite Quick Start Script for Windows

echo.
echo 🚀 MarketAI Suite - Quick Start
echo ===============================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.9+
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo ✓ Python found: %PYTHON_VERSION%
echo.

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📚 Installing dependencies...
pip install -r requirements.txt

echo.
echo ===============================
echo Setup complete! You can now run:
echo     python app.py
echo.
echo The app will be available at:
echo     http://localhost:5000
echo.
echo Test credentials:
echo     Email: test@example.com
echo     Password: (register a new account)
echo ===============================
echo.
pause
