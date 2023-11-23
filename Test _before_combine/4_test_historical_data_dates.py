import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timedelta

DAY1 = 5

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

# Select target currency
target_currency = st.selectbox("Select target currency", selected_currencies)


def fetch_exchange_rate(base, target, date):
    """
    Fetches the exchange rate for a given date.
    """
    formatted_date = date.strftime("%Y-%m-%d")
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{formatted_date}/currencies/{base.lower()}/{target.lower()}.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get(target.lower())
    return None


# Buttons for selecting time frame
if st.button("1 Days"):
    days_to_fetch = 1
elif st.button("3 Days"):
    days_to_fetch = 3
elif st.button("5 Days"):
    days_to_fetch = 5
elif st.button("15 Days"):
    days_to_fetch = 15
else:
    # Default value or a message to select an option
    days_to_fetch = 0

# Fetch data for the past days
data = []
for i in range(days_to_fetch):
    date = datetime.now() - timedelta(days=i)
    rate = fetch_exchange_rate(base_currency, target_currency, date)
    if rate is not None:
        data.append({"date": date.strftime("%Y-%m-%d"), "rate": rate})

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the Dataframe
st.write(df)
