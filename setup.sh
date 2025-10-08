#!/bin/bash

echo "🎯 Darts Scorer App - IONOS Setup Script"
echo "========================================"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python 3 found"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Test database connection
echo "🗄️ Testing database connection..."
python3 -c "
import os
from dotenv import load_dotenv
load_dotenv()
import pymysql

try:
    connection = pymysql.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT', 3306)),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        connect_timeout=10
    )
    print('✅ Database connection successful!')
    connection.close()
except Exception as e:
    print(f'❌ Database connection failed: {e}')
    exit(1)
"

if [ $? -eq 0 ]; then
    echo ""
    echo "🚀 Setup completed successfully!"
    echo ""
    echo "To start the application:"
    echo "1. source venv/bin/activate"
    echo "2. python src/main.py"
    echo ""
    echo "For production deployment:"
    echo "1. pip install gunicorn"
    echo "2. gunicorn --bind 0.0.0.0:5000 --chdir src main:app"
    echo ""
    echo "Your darts scoring app will be available at http://your-server:5000"
else
    echo "❌ Setup failed. Please check your database credentials in .env file"
    exit 1
fi
