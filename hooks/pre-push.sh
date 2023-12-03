#!/bin/bash

# Get the current branch
current_branch=$(git rev-parse --abbrev-ref HEAD)

# Check if it's not the default branch (e.g., main/master)
if [ "$current_branch" != "main" ] && [ "$current_branch" != "master" ]; then
    echo "Running pre-push checks on branch '$current_branch'..."

    # Run black
    echo "Running black..."
    black .

    # Run isort
    echo "Running isort..."
    isort .

    # Run flake8
    echo "Running flake8..."
    flake8 .

    # Run mypy
    echo "Running mypy..."
    mypy .

    # If any of the checks fail, prevent the push
    if [ $? -ne 0 ]; then
        echo "Pre-push checks failed. Please fix the issues before pushing."
        exit 1
    fi

    echo "Pre-push checks passed successfully."
fi

# Continue with the push
exit 0
