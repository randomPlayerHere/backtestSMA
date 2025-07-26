import pandas as pd
import numpy as np

class stratergy:
    def generate_signals(self, data):
        raise NotImplemented

# SIMPLE MOVING AVERAGE STRATERGY
class sma(stratergy):
    def __init__(self, sma_length, lma_length):
        self.short_moving_average=sma_length
        self.long_moving_average = lma_length

    def calculate_smas(self,data):
        signals = pd.DataFrame(index=data.index)
        closing_price = data['Close']
        signals['price'] = closing_price
        signals['sma'] = closing_price.rolling(window=self.short_moving_average, min_period=1).mean()
        signals['lma'] = closing_price.rolling(window=self.long_moving_average, min_period=1).mean()
        return signals

    def generate_signals(self,data):
        signals = self.calculate_smas()
        #Buy Signal
        signals['signal'][20:] = np.where((signals['sma'][20:] > signals['lma'][20:]) & (signals['sma'].shift(1)[20:] <= signals['lma'].shift(1)[20:]),1.0, 0.0)
        #Sell Signal
        signals['signal'][20:] = np.where((signals['sma'][20:] < signals['lma'][20:]) & (signals['sma'].shift(1)[20:]>= signals['lma'].shift(1)[20:]), -1.0, signals['signal'][20:])
        signals['positions'] = signals['signal'].diff()
        return signals
