import os

import alpaca_trade_api as tradeapi # type: ignore
import pandas as pd
from ta import add_all_ta_features # type: ignore
from ta.utils import dropna # type: ignore

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

df = api.get_bars("SPY", tradeapi.TimeFrame.Day, "2021-06-01", "2021-10-01").df

# Clean NaN values
df = dropna(df)

# Add ta features filling NaN values
df = add_all_ta_features(
    df,
    open="Open",
    high="High",
    low="Low",
    close="Close",
    volume="Volume_BTC",
    fillna=True,
)
