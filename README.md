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
- Python
- pandas
- yfinance
- matplotlib

## Future Improvements
- Parameter optimization (grid search)
- Add slippage/transaction costs
- Support for other indicators (e.g. RSI, MACD)
- Use backtesting libraries (e.g., Backtrader)

## Structure

