import pandas as pd

class Backtest:
    def __init__(self, initial_capital=100000):
        self.initial_capital = initial_capital

    def run(self, data, signals):
        positions = pd.DataFrame(index=signals.index)
        positions['position'] = signals['positions']
        positions['price'] = data['Close']
        positions['trade'] = positions['position'].diff().fillna(positions['position'])
        positions['cash'] = self.initial_capital - (positions['trade'] * positions['price']).cumsum()
        positions['holdings'] = positions['position'] * positions['price']
        positions['total'] = positions['cash'] + positions['holdings']
        positions['returns'] = positions['total'].pct_change().fillna(0)
        return positions
