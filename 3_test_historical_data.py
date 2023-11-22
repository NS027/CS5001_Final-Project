import streamlit as st
import requests
from datetime import datetime, timedelta

selected_currencies = [
    "CNY",
    "USD",
    "HKD",
    "GBP",
    "AUD",
    "JPY",
    "EUR",
    "CAD",
    "SGD",
    "NZD",
    "CHF",
]

# Select base currency
base_currency = st.selectbox("Select base currency", selected_currencies)

# Assuming you want to convert to a target currency, add a selection for this too
target_currency = st.selectbox("Select target currency", selected_currencies)

# Get yesterday's date
yesterday = datetime.now() - timedelta(days=1)
date_str = yesterday.strftime("%Y-%m-%d")

# Construct the API URL
url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{date_str}/currencies/{base_currency.lower()}/{target_currency.lower()}.json"

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Display the data and its type in Streamlit
    st.write("Data:", data)
    st.write("Type of Data:", type(data))
else:
    st.error("Failed to retrieve data")
