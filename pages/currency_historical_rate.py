"""
Final Porject

This file contains the function that displays the historical currency rate.
"""
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from models.selected_currency import SelectedCurrency
from models.fetch_currency_data import CurrencyData


def display_historical_currency_rate():
    """
    Function -- display_historical_currency_rate
        Display the historical currency rate
    Parameters:
        None
    Returns:
        None
    """
    # Create an instance of CurrencyData
    currency_data = CurrencyData()

    # Set the select box value
    select_box_value = SelectedCurrency.selected_currencies

    # Set the base currency
    base_currency = st.selectbox("Base currency", select_box_value)
    # Set the target currency
    target_currency = st.selectbox("Target currency", select_box_value)

    # Initialize the date to 0
    days_to_fetch = 0

    # Buttons for selecting the time period
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Three Day"):
            days_to_fetch = 3
    with col2:
        if st.button("One Week"):
            days_to_fetch = 7
    with col3:
        if st.button("Half Month"):
            days_to_fetch = 15
    with col4:
        if st.button("One Month"):
            days_to_fetch = 30

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
            # Sort the dataframe by the "Date" column in descending order
            df = df.sort_values(by="Date", ascending=False)
            # Display the dataframe without the index column
            st.dataframe(df.set_index("Date"))
        else:
            st.error("No historical data available for the selected period.")
    else:
        # This will leave the space blank if no time period is selected
        st.write("Select a time period and currencies to view historical rates.")


if __name__ == "__main__":
    display_historical_currency_rate()
