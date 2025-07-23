import yfinance as yf
dat = yf.Ticker("RELIANCE.NS")
print(dat.history(period='5mo'))