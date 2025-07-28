import matplotlib.pyplot as plt

def plot_strategy(signals, ticker):
    plt.figure(figsize=(12,6))
    plt.plot(signals['price'], label='Price', alpha=0.5)
    plt.plot(signals['sma'], label='20-day SMA', alpha=0.75)
    plt.plot(signals['lma'], label='50-day SMA', alpha=0.75)
    plt.plot(signals.loc[signals.signal == 1.0].index,signals.sma[signals.signal == 1.0],'^', markersize=10, color='g', label='Buy')
    plt.plot(signals.loc[signals.signal == -1.0].index,signals.sma[signals.signal == -1.0],'v', markersize=10, color='r', label='Sell')
    plt.title(f'{ticker} SMA Trading Strategy')
    plt.legend()
    plt.show()