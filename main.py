import streamlit as st
from datetime import datetime

def calculate_spread(agreed_price, trading_price):
    return ((agreed_price - trading_price) / trading_price) * 100

def calculate_annualized_spread(spread, close_date):
    today = datetime.today().date()
    # close_date = datetime.strptime(close_date, '%Y-%m-%d')
    days_to_close = (close_date - today).days
    annualized_spread = (spread * 365) / days_to_close if days_to_close > 0 else 0
    return annualized_spread

def calculate_leveraged_return(spread, leverage, margin_rate):
    return leverage * (spread - margin_rate)

def calculate(agreed_price, trading_price, close_date):

    spread = calculate_spread(agreed_price, trading_price)

    annualized_spread = calculate_annualized_spread(spread, close_date)

    margin_rates = [1.5, 2.0, 5.5]
    leveraged_returns_3x = [calculate_leveraged_return(annualized_spread, 3, rate) for rate in margin_rates]
    leveraged_returns_4x = [calculate_leveraged_return(annualized_spread, 4, rate) for rate in margin_rates]

    return spread, annualized_spread, leveraged_returns_3x, leveraged_returns_4x

st.title('Arbitrage Spread Calculator')

col1, col2, col3 = st.columns(3)
agreed_price = col1.number_input('Agreed Price (USD)', min_value=0.0, step=0.01)
trading_price = col2.number_input('Trading Price (USD)', min_value=0.0, step=0.01)
close_date = col3.date_input('Close Date', min_value=datetime.today(), format="DD/MM/YYYY")

col1, col2, col3 = st.columns(3)

if col2.button('Calculate Spreads'):
    if trading_price > 0:
        spread = calculate_spread(agreed_price, trading_price)
        st.write(f"**Spread**: {spread:.2f}%")

        annualized_spread = calculate_annualized_spread(spread, close_date)
        st.write(f"**Annualized Spread**: {annualized_spread:.2f}%")

        col1, col2 = st.columns(2)
        
        margin_rates = [1.5, 2.0, 5.5]
        col1.write("### Leverage 3x")
        for rate in margin_rates:
            leveraged_return_3x = calculate_leveraged_return(annualized_spread, 3, rate)
            col1.write(f"Margin Rate {rate}%: {leveraged_return_3x:.2f}%")

        col2.write("### Leverage 4x")
        for rate in margin_rates:
            leveraged_return_4x = calculate_leveraged_return(annualized_spread, 4, rate)
            col2.write(f"Margin Rate {rate}%: {leveraged_return_4x:.2f}%")
    else:
        st.error('Trading price must be greater than 0.')
