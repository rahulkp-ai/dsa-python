#!/usr/bin/env bash
set -e
echo "🚀 Setting up DSA-Python..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip -q
pip install -r requirements.txt -q
pip install -e . -q
find src -type d -exec touch {}/__init__.py \;
find tests -type d -exec touch {}/__init__.py \;
echo "✅ Setup complete! Run: source venv/bin/activate"
