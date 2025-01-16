import yfinance as yf
import pandas as pd
import os

DATA_DIR = "./data/raw"

os.makedirs(DATA_DIR, exist_ok=True)

tickers = ["AAPL", "MSFT", "TSLA", "GOOG", "NVDA"]

for ticker in tickers:
    print("Fetching data for", ticker)
    data = yf.download(ticker, start="2020-01-01", end="2025-01-01")
    filepath = os.path.join(DATA_DIR, f"{ticker}.csv")
    data.to_csv(filepath)
    print(f"Data for {ticker} saved to {filepath}")