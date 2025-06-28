# Circle Developer-Controlled Wallets Quickstart

This project follows the Circle Interactive Quickstart for Developer-Controlled Wallets using Python.

## Prerequisites

- Python 3.7+
- Circle Developer Account
- API Key and Entity Secret from Circle Console

## Setup

1. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set environment variables:
```bash
export CIRCLE_API_KEY="your_api_key_here"
export CIRCLE_ENTITY_SECRET="your_entity_secret_here"
```

## Usage

Run the quickstart:
```bash
python main.py
```

## Steps

The quickstart includes the following steps:
1. Create a wallet set
2. Create a wallet
3. Get wallet balance
4. Create a transaction
5. Sign a transaction

## Files

- `main.py` - Main script that orchestrates the quickstart
- `steps.py` - Individual step functions
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Reference

[Circle Interactive Quickstart](https://developers.circle.com/interactive-quickstarts/dev-controlled-wallets) 