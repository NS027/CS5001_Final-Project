import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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


def fetch_historical_data(base, target, date):
    """
    - Fuctions: Fetches the exchange rate for a given date.
    - Parameters:
        base: the base currency
        target: the target currency
        date: the date choose from the date picker
    - Returns: exchange rate
    """
    formatted_date = date.strftime("%Y-%m-%d")
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{formatted_date}/currencies/{base.lower()}/{target.lower()}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get(target.lower())
    return None


def plot_with_dynamic_y_axis(df, base_currency, target_currency):
    """
    - Functions: Plots the exchange rate for a given base and target currency.
    - Parameters:
        df: the dataframe with exchange rate data
        base_currency: the base currency
        target_currency: the target currency
    - Returns: None
    """
    y_min = df["rate"].min() * 0.99  # 1% margin at the bottom
    y_max = df["rate"].max() * 1.01  # 1% margin at the top
    plt.figure(figsize=(10, 6))
    # Plot the exchange rate
    plt.plot(
        df["date"],
        df["rate"],
        color="black",
        marker="",
        linestyle="solid",
        linewidth=2,
        markersize=6,
    )
    plt.ylim(y_min, y_max)
    plt.title(f"Exchange rate trend from {base_currency} to {target_currency}")
    plt.xlabel("Date")
    plt.ylabel("Exchange rate")
    plt.xticks(rotation=45)
    plt.grid(False)
    plt.tight_layout()
    st.pyplot(plt)


def fetch_exchange_data(base_currency, target_currency):
    """
    - Functions: Fetches the exchange rate for a given base and target currency.
    - Parameters:
        base_currency: the base currency
        target_currency: the target currency
        days_to_fetch: the number of days to fetch
    - Returns: dataframe with exchange rate data
    """
    days_to_fetch = st.radio("Select time frame", [1, 3, 5, 15])

    data = []
    if base_currency and target_currency and days_to_fetch:
        for i in range(days_to_fetch):
            date = datetime.now() - timedelta(days=i)
            rate = fetch_historical_data(base_currency, target_currency, date)
            if rate is not None:
                data.append({"date": date.strftime("%Y-%m-%d"), "rate": rate})

        df = pd.DataFrame(data)
        if not df.empty:
            df["date"] = pd.to_datetime(df["date"])
            df = df.sort_values(by="date")
            plot_with_dynamic_y_axis(df, base_currency, target_currency)
        else:
            st.write("No data available for the selected currency pair.")


def main():
    # Select base currency
    base_currency = st.selectbox("Select base currency", selected_currencies)

    # Select target currency
    target_currency = st.selectbox("Select target currency", selected_currencies)

    fetch_exchange_data(base_currency, target_currency)
    st.write("Data source: https://github.com/fawazahmed0/currency-api#readme")


if __name__ == "__main__":
    main()
