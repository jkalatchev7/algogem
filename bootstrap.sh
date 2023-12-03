#!/bin/bash

# Set the Python version
PYTHON_VERSION=3.10

# Create a virtual environment
python${PYTHON_VERSION} -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install the required packages
pip install black isort flake8

# Copy git push hook
cp hooks/pre-push.sh .git/hooks/pre-push

# Add bash alias
echo 'alias algo="cd ~/personal/algogem && source venv/bin/activate"' >> ~/.bash_aliases


