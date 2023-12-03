import os

import alpaca_trade_api as tradeapi  # type: ignore

# Verify API's work by checking for expected account id
api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")

# Replace 'your_api_key' and 'your_api_secret' with your actual Alpaca API key and secret
base_url = "https://paper-api.alpaca.markets"  # For paper trading
api = tradeapi.REST(api_key, api_secret, base_url, api_version="v2")

# Get account information
account = api.get_account()
print(f"Account ID: ${account.id}")
print(f"Buying Power: ${account.buying_power}")
print(f"Equity: ${account.equity}")
