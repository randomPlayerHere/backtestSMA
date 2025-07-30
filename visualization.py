import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_strategy(signals, ticker):
    fig = plt.figure(figsize=(12,6))
    plt.plot(signals['price'], label='Price', alpha=0.5)
    plt.plot(signals['sma'], label='20-day SMA', alpha=0.75)
    plt.plot(signals['lma'], label='50-day SMA', alpha=0.75)
    plt.plot(signals.loc[signals.signal == 1.0].index,signals.sma[signals.signal == 1.0],'^', markersize=10, color='g', label='Buy')
    plt.plot(signals.loc[signals.signal == -1.0].index,signals.sma[signals.signal == -1.0],'v', markersize=10, color='r', label='Sell')
    plt.title(f'{ticker} SMA Trading Strategy')
    plt.legend()
    return fig


def create_performance_chart(data, signals, results, short_ma, long_ma, ticker, capital):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [2, 1]})
    dates = data.index
    ax1.plot(dates, data['Close'], label='Close Price', color='black', linewidth=1.5)
    ax1.plot(dates, signals['sma'], label=f'SMA ({short_ma})', color='blue', linewidth=1.2)
    ax1.plot(dates, signals['lma'], label=f'LMA ({long_ma})', color='red', linewidth=1.2)
    buy_signals = signals[signals['signal'] == 1.0]
    sell_signals = signals[signals['signal'] == -1.0]
    
    if not buy_signals.empty:
        ax1.scatter(buy_signals.index, buy_signals['price'], 
                    color='green', marker='^', s=100, label='Buy Signal', zorder=5)
    
    if not sell_signals.empty:
        ax1.scatter(sell_signals.index, sell_signals['price'], 
                    color='red', marker='v', s=100, label='Sell Signal', zorder=5)
    
    ax1.set_title(f'{ticker} - SMA Strategy Performance', fontsize=16, fontweight='bold')
    ax1.set_ylabel('Price (₹)', fontsize=12)
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    
    ax2.plot(dates, results['total'], label='Portfolio Value', color='green', linewidth=2)
    ax2.axhline(y=capital, color='gray', linestyle='--', alpha=0.7, label='Initial Capital')
    
    ax2.set_title('Portfolio Value Over Time', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylabel('Portfolio Value (₹)', fontsize=12)
    ax2.legend(loc='upper left')
    ax2.grid(True, alpha=0.3)
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x:,.0f}'))

    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
    
    plt.tight_layout()
    return fig