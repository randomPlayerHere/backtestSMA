import yfinance as yf

class DataLoader:
    def __init__(self, ticker, start,end):
        self.ticker = ticker
        self.start_date = start
        self.end_date = end
    def fetch_data(self):
        return yf.download(self.ticker, start=self.start_date, end=self.end_date)