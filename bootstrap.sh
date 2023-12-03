#!/bin/bash

# Exit immediately if any command fails
set -e

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install the required packages
pip install black isort mypy flake8 alpaca-trade-api yfinance ta pytest types-PyYAML

# Copy git push hook
cp hooks/pre-push.sh .git/hooks/pre-push
chmod +x .git/hooks/pre-push

# Add bash alias
echo 'alias algo="cd ~/personal/algogem && source venv/bin/activate"' >> ~/.bash_aliases


