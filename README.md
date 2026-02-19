# Simple Moving Average (SMA) Strategy Backtest 

This project demonstrates how to backtest a simple moving average (SMA) crossover trading strategy using Python. The strategy buys when the short-term SMA crosses above the long-term SMA and sells when it crosses below.

## Features
- SMA crossover strategy logic
- Historical stock data download
- Trading signal generation
- Performance metrics: cumulative returns, Sharpe ratio, drawdown
- Comparison with buy-and-hold
- Visualization of price, signals, and returns

## Strategy Logic
- **Buy Signal**: Short-term SMA > Long-term SMA
- **Sell Signal**: Short-term SMA < Long-term SMA
- Example: 50-day SMA and 200-day SMA crossover

## Tools & Libraries
- Python, pandas, yfinance, matplotlib, Streamlit

## Structure
```
├── app.py              # Streamlit UI
├── data_handler.py     # Fetch stock data
├── strategies.py       # SMA strategy logic
├── backtester.py       # Backtest engine
├── visualization.py    # Charts
└── requirements.txt
```

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy
Push to GitHub → Deploy on [Streamlit Cloud](https://share.streamlit.io)

