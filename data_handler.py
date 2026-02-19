import yfinance as yf


def fetch_data(ticker, start_date, end_date):
    return yf.download(ticker, start=start_date, end=end_date, auto_adjust=True, progress=False)
    
if __name__ == "__main__":
    ticker = input("Enter the ticker symbol (.NS at end if indian stock)").upper()
    start_date = input("Enter the start date(YYYY-MM-DD): ")
    end_date = input("Enter the end date(YYYY-MM-DD): ")
    data = fetch_data(ticker, start_date,end_date)
    # print(data['Close'])