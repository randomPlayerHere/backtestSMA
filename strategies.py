import pandas as pd
import numpy as np

class strategy:
    def generate_signals(self, data):
        raise NotImplemented

# SIMPLE MOVING AVERAGE strategy
class sma(strategy):
    def __init__(self, sma_length, lma_length):
        self.short_moving_average=sma_length
        self.long_moving_average = lma_length

    def calculate_smas(self,data):
        signals = pd.DataFrame(index=data.index)
        closing_price = data['Close']
        signals['price'] = closing_price
        signals['sma'] = closing_price.rolling(window=self.short_moving_average, min_periods=1).mean()
        signals['lma'] = closing_price.rolling(window=self.long_moving_average, min_periods=1).mean()
        return signals
    

    def generate_signals(self,data):
        signals = self.calculate_smas(data)
        signals['signal'] = 0.0
        start_idx = max(self.short_moving_average, self.long_moving_average)
        # Buy Signal
        signals.loc[start_idx:, 'signal'] = np.where(
            (signals['sma'][start_idx:] > signals['lma'][start_idx:]) & 
            (signals['sma'].shift(1)[start_idx:] <= signals['lma'].shift(1)[start_idx:]), 
            1.0, 0.0
        )
        #Sell Signal
        signals.loc[start_idx:, 'signal'] = np.where(
            (signals['sma'][start_idx:] < signals['lma'][start_idx:]) & 
            (signals['sma'].shift(1)[start_idx:] >= signals['lma'].shift(1)[start_idx:]), 
            -1.0, 
            signals['signal'][start_idx:]
        )
        signals['positions'] = signals['signal'].diff()
        return signals
