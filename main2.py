import streamlit as st
from data_handler import *
from strategies import *
from visualization import *
from backtester import *


st.title("Simple Moving Average (SMA) Strategy Backtest")
st.write("### Set Conditions")

col1, col2 = st.columns(2)
ticker = st.text_input("Ticker Symbol (add .NS at the end for Indian Stocks)")
capital = st.number_input("Initial Capital", value=100000)
start_date_input = col1.date_input("Start Date")
end_date_input = col2.date_input("End Date")
col3, col4 = st.columns(2)
short_ma = col3.number_input("Short Moving Average (days)", value=20, min_value=1, max_value=200)
long_ma = col4.number_input("Long Moving Average (days)", value=50, min_value=1, max_value=200)



calculate_button = st.button("Calculate Backtest", type="primary")

def format_currency(amount):
    return f"₹{amount:,.2f}"

def format_percentage(pct):
    return f"{pct:+.2f}%"


st.write("### Results")
if calculate_button:
    if not ticker:
        st.error("Please enter a ticker symbol")
    elif start_date_input >= end_date_input:
        st.error("Start date must be before end date")
    elif short_ma >= long_ma:
        st.error("Short MA must be less than Long MA")
    else:
        start_date = start_date_input.strftime("%Y-%m-%d")
        end_date = end_date_input.strftime("%Y-%m-%d")

        data_reliance = fetch_data(ticker=ticker, start_date=start_date, end_date=end_date)
        sma1 = sma(sma_length=short_ma, lma_length=long_ma)
        signals_reliance = sma1.generate_signals(data=data_reliance)
        bt = Backtest(initial_capital=capital)
        results = bt.run(data_reliance, signals_reliance)

        final_capital = results['total'].iloc[-1]
        total_return_pct = ((final_capital - capital) / capital) * 100
        
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Initial Capital", value=format_currency(capital))
        col2.metric(label="Final Capital", value=format_currency(final_capital))
        col3.metric(label="Total Return", value=format_percentage(total_return_pct), 
                   delta=format_percentage(total_return_pct))
        
        st.write("### Strategy Parameters")
        param_col1, param_col2 = st.columns(2)
        param_col1.write(f"**Ticker:** {ticker}")
        param_col1.write(f"**Start Date:** {start_date}")
        param_col1.write(f"**End Date:** {end_date}")
        param_col2.write(f"**Short MA:** {short_ma} days")
        param_col2.write(f"**Long MA:** {long_ma} days")
        param_col2.write(f"**Initial Capital:** {format_currency(capital)}")
        
        st.write("### Performance Chart")
        chart_fig = create_performance_chart(data_reliance, signals_reliance,results,short_ma, long_ma, ticker, capital)

        st.pyplot(chart_fig)
        
        
else:
    st.info("Enter your parameters above and click 'Calculate Backtest' to see results")
