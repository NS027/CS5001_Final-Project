"""
Final Project

This file contains the function that converts the currency.
"""
import streamlit as st
from models.selected_currency import SelectedCurrency
from models.fetch_currency_data import CurrencyData


def convert_currency():
    """
    Function -- convert_currency
        Convert the currency
    Parameters:
        from_currency -- the currency that the user want to convert from
        to_currency -- the currency that the user want to convert to
        amount -- the amount that the user want to convert
    Returns:
        A float that contains the converted amount
    """
    # Set the page title
    st.markdown(
        '<p style="font-family: Georgia; color:#025167; font-size: 36px; font-weight: bold;">Currency Convertor</p>',
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
        '<p style="font-family:Georgia; text-align: justify; color:#ARRGGBB; font-size: 15px; font-weight: normal;">The Currency Converter delivers instantaneous and precise currency conversions, utilizing up-to-the-minute exchange rates for dependable financial transactions.</p>',
        unsafe_allow_html=True,
    )

    # Create an instance of CurrencyData
    currency_data = CurrencyData()

    # Create an instance of SelectedCurrency
    selected_currency = SelectedCurrency()

    # Get the entered amount from the user
    amount = st.number_input("Enter the amount: ")
    # Set the select box value
    select_box_value = selected_currency.get_selected_currencies()

    # Set the select box
    select_from_currency = st.selectbox("From currency", select_box_value)
    select_to_currency = st.selectbox("To currency", select_box_value)

    from_currency = select_from_currency.lower()
    to_currency = select_to_currency.lower()

    # Display the conversion result
    if st.button("Convert", key="convert_button"):
        # Get the exchange rate from the API
        exchange_rate = currency_data.get_exchange_rate(from_currency, to_currency)

        if exchange_rate is not None:
            # Convert the currency
            converted_amount = amount * exchange_rate

            # Get the currency abbreviation
            abbreviation = currency_data.get_abbreviation()
            from_currency_name = abbreviation.get(from_currency.upper(), "None")
            to_currency_name = abbreviation.get(to_currency.upper(), "None")
            st.success(
                f"{amount} {from_currency_name} is {converted_amount:.2f} {to_currency_name}"
            )
        else:
            st.error("Failed to get the exchange rate.")


if __name__ == "__main__":
    convert_currency()
