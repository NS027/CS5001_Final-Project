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

    # Set the page title
    st.markdown(
        '<p style="font-family: Georgia; color:#025167; font-size: 36px; font-weight: bold;">Currency Historical Rate</p>',
        unsafe_allow_html=True,
    )
    # Add a divider
    st.markdown(
        """
    <div style='height: 3px; background-color: #3A3B3C; margin-top: 0px; margin-bottom: 3px;'></div>
    <div style='height: 2px; background-color: #3A3B3C; margin-top: 0px; margin-bottom: 5px;'></div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p style="font-family:Georgia; text-align: justify; color:#ARRGGBB; font-size: 15px; font-weight: normal;">Explore the Currency Historical Rate feature to trace and analyze past exchange rate trends, providing valuable insights for strategic financial planning and market analysis.</p>',
        unsafe_allow_html=True,
    )

    # Create an instance of CurrencyData
    currency_data = CurrencyData()

    # Create an instance of SelectedCurrency
    selected_currency = SelectedCurrency()

    # Set the select box value
    select_box_value = selected_currency.get_selected_currencies()

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
            # Create the DataFrame
            df = pd.DataFrame(data)

            # Define the styles for table headers and data cells
            s1 = dict(selector="th", props=[("text-align", "center")])
            s2 = dict(selector="td", props=[("text-align", "center")])

            # Create the Styler object and apply the formatting
            styler = df.style.set_table_styles([s1, s2]).hide(axis=0)
            styler = styler.format({"Rate": "{:.2f}", "Buy Rate": "{:.2f}"})
            df_html = styler.to_html(escape=False)

            # Use columns to control the layout
            col1, col2, col3 = st.columns([2, 3, 1])
            with col2:
                st.write(df_html, unsafe_allow_html=True)
        else:
            st.error("No historical data available for the selected period.")
    else:
        # This will leave the space blank if no time period is selected
        st.write("Select a time period and currencies to view historical rates.")


if __name__ == "__main__":
    display_historical_currency_rate()
