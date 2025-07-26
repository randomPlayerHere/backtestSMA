import yfinance as yf

class DataLoader:
    def __init__(self, ticker, start,end):
        self.ticker = ticker
        self.start_date = start
        self.end_date = end
    def fetch_data(self):
        return yf.download(self.ticker, start=self.start_date, end=self.end_date, auto_adjust=True)
    
if __name__ == "__main__":
    ticker = input("Enter the ticker symbol (.NS at end if indian stock)").upper()
    start_date = input("Enter the start date(YYYY-MM-DD): ")
    end_date = input("Enter the end date(YYYY-MM-DD): ")
    dataload = DataLoader(ticker, start_date,end_date)
    data = dataload.fetch_data()
    # print(data['Close'])