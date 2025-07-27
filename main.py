from data_handler import *
from stratergies import *
from visualization import *

if __name__ == "__main__":
    ticker = "AAPL"
    start = "2020-01-01"
    end = "2024-01-01"
    data_reliance = fetch_data(ticker=ticker, start_date=start, end_date=end)
    sma1 = sma(sma_length=20, lma_length=50)
    signals_reliance = sma1.generate_signals(data=data_reliance)
    plot_strategy(signals=signals_reliance, ticker=ticker)
