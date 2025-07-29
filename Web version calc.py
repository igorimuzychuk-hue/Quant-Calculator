import streamlit as st

st.title("Simplified Quant Calculator")

# Input fields
rsi = st.number_input("RSI Value", value=50.0)
moving_average = st.number_input("Current Moving Average", value=0.0)
macd = st.number_input("Current MACD", value=0.0)

# Function to calculate the trade decision
def calculate_trade_decision(rsi, moving_average, macd):
    score = 0

    # RSI logic
    if rsi < 30:
        score += 1
    elif rsi > 70:
        score -= 1

    # Moving Average logic
    if moving_average > 0:
        score += 1
    elif moving_average < 0:
        score -= 1

    # MACD logic
    if macd > 0:
        score += 1
    elif macd < 0:
        score -= 1

    # Final decision
    if score == 3:
        return "Strong Buy"
    elif score == -3:
        return "Strong Sell"
    elif score > 0:
        return "Weak Buy"
    elif score < 0:
        return "Weak Sell"
    else:
        return "Hold"

# Button and output
if st.button("Calculate"):
    decision = calculate_trade_decision(rsi, moving_average, macd)
    st.subheader(f"Recommendation: {decision}")