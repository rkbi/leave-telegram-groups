# Telegram Group Leave Script

This script helps you leave groups in Telegram using the `Telethon` library.

## Prerequisites

- **Python 3.8+**: Ensure you have Python installed.
- **UV**: The package manager for Python environments (`uv`).
- Collect your API ID from https://my.telegram.org/auth

## Setup Instructions

1. **Create a Virtual Environment**
   Run the following command to create a virtual environment:
   ```bash
   uv venv .venv

2. **Activate the Virtual Environment**
   Activate the Virtual Environment If you're using the Fish shell, activate the environment with:
   ```bash
   source .venv/bin/activate.fish

3. **Install Dependencies**
   Install Dependencies Install the required dependencies (e.g., Telethon):
   ```bash
   uv pip install telethon

4. **Run the Script**
    Run the Script After installation, run the Python script to leave Telegram groups:   
    ```bash
   python leave.py

5. **Get Your API ID and API Hash**
   Visit https://my.telegram.org/auth to get your API credentials (API ID and API Hash) and replace the placeholders in the `config.ini` file.
