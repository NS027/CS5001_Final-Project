"""
Final Project

This file contains the function that displays line chart of currency rate.
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from models.selected_currency import SelectedCurrency
from models.fetch_currency_data import CurrencyData


def currency_line_chart():
    """
    Fuctions -- currency_line_chart
        Display the line chart of currency rate.
    Parameters:
        None
    Returns:
        None
    """
    # Create an instance of CurrencyData
    currency_data = CurrencyData()

    # Add a title
    st.title("Currency Line Chart")

    # Add a description
    st.write(
        "This page displays the line chart of currency rate. You can select the currency and the time period."
    )

    # Set the select box value
    select_box_value = SelectedCurrency.selected_currencies

    # Select base currency
    base_currency = st.selectbox("Select base currency", select_box_value)
    # Select target currency
    target_currency = st.selectbox("Select target currency", select_box_value)

    # Set the default time period to 0
    days_to_fetch = 0

    # Buttons for selecting the time period
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Three Days"):
            days_to_fetch = 3
    with col2:
        if st.button("Five Days"):
            days_to_fetch = 5
    with col3:
        if st.button("Seven Days"):
            days_to_fetch = 7
    with col4:
        if st.button("Half Month"):
            days_to_fetch = 15

    if days_to_fetch > 0:
        # Fetch the historical currency rate data
        data = []
        for i in range(days_to_fetch):
            date = datetime.now() - timedelta(days=i)
            historical_rate = currency_data.get_currency_historical_data(
                base_currency, target_currency, date
            )
            if historical_rate is not None:
                data.append(
                    {"Date": date.strftime("%Y-%m-%d"), "Rate": historical_rate}
                )

        # Check if data is not empty before creating the DataFrame
        if data:
            df = pd.DataFrame(data)
            # Convert the "Date" column to datetime
            df["Date"] = pd.to_datetime(df["Date"])
            # Sort the dataframe by the "Date" column in descending order
            df = df.sort_values(by="Date")
            # Distpaly the line chart
            set_the_pilot(df, base_currency, target_currency)
        else:
            st.error("No historical data available for the selected period.")
    else:
        # This will leave the space blank if no time period is selected
        st.write("Select a time period and currencies to view line chart.")


def set_the_pilot(df, base_currency, target_currency):
    """
    Function -- set_the_pilot
        Display the line chart of currency rate.
    Parameters:
        df -- the dataframe that contains the currency rate data
        base_currency -- the currency that the user want to convert from
        target_currency -- the currency that the user want to convert to
    Returns:
        None
    """
    y_min = df["Rate"].min() * 0.99  # 1% margin at the bottom
    y_max = df["Rate"].max() * 1.01  # 1% margin at the top
    plt.figure(figsize=(10, 6))
    # Plot the exchange rate
    plt.plot(
        df["Date"],  # X values
        df["Rate"],  # Y values
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
    plt.grid(False)  # Do not display the grid
    plt.tight_layout()
    st.pyplot(plt)


if __name__ == "__main__":
    currency_line_chart()
