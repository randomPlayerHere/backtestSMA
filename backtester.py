import pandas as pd

class Backtest:
    def __init__(self, initial_capital=100000):
        self.initial_capital = initial_capital

    def run(self, data, signals):
        positions = pd.DataFrame(index=signals.index)
        positions['position'] = signals['positions']  # ← Use actual held position, not just trigger
        positions['price'] = data['Close']
        
        # Portfolio value = position * price
        positions['holdings'] = positions['position'] * positions['price']
        
        # Assume cash decreases when we buy, increases when we sell
        positions['cash'] = self.initial_capital - (positions['position'].diff().fillna(0) * positions['price']).cumsum()

        # Total portfolio value = cash + holdings
        positions['total'] = positions['cash'] + positions['holdings']
        
        # Daily returns (optional)
        positions['returns'] = positions['total'].pct_change().fillna(0)

        return positions
