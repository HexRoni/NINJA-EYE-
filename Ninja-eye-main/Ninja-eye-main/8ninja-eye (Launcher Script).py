#!/bin/bash
# NINJA EYE Launcher Script
# This script activates the virtual environment and runs the program.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/venv"

# Check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "❌ Virtual environment not found!"
    echo ""
    echo "Run the setup first:"
    echo "  cd $SCRIPT_DIR"
    echo "  python3 -m venv venv"
    echo "  source venv/bin/activate"
    echo "  pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment and run
source "$VENV_DIR/bin/activate"
python3 "$SCRIPT_DIR/ninja_eye.py"
