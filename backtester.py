import pandas as pd

class Backtest:
    def __init__(self, initial_capital=100000):
        self.initial_capital = initial_capital

    def run(self, data, signals):
        positions = pd.DataFrame(index=signals.index)
        positions['position'] = signals['positions']
        positions['price'] = data['Close']

        # Calculate trades (difference in position)
        positions['trade'] = positions['position'].diff().fillna(positions['position'])

        # Calculate cash: subtract cost when buying, add when selling
        positions['cash'] = self.initial_capital - (positions['trade'] * positions['price']).cumsum()

        # Holdings: current position * price
        positions['holdings'] = positions['position'] * positions['price']

        # Total portfolio value
        positions['total'] = positions['cash'] + positions['holdings']

        # Daily returns
        positions['returns'] = positions['total'].pct_change().fillna(0)

        return positions
