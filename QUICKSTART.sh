#!/bin/bash
# MarketAI Suite Quick Start Script

echo "🚀 MarketAI Suite - Quick Start"
echo "================================"
echo ""

# Check Python
if ! command -v python &> /dev/null; then
    echo "❌ Python not found. Please install Python 3.9+"
    exit 1
fi

echo "✓ Python found: $(python --version)"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "================================"
echo "Setup complete! You can now run:"
echo "    python app.py"
echo ""
echo "The app will be available at:"
echo "    http://localhost:5000"
echo ""
echo "Test credentials:"
echo "    Email: test@example.com"
echo "    Password: (register a new account)"
echo "================================"
