"""
Final Project

This file contains the function that converts the currency.
"""
import streamlit as st
from models.selected_currency import SelectedCurrency
from models.fetch_currency_data_copy import CurrencyData

# from models.fetch_currency_data import get_exchange_rate, get_abbreviaton


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
    # Create an instance of CurrencyData
    currency_data = CurrencyData()

    # Get the entered amount from the user
    amount = st.number_input("Enter the amount: ")
    # Set the select box value
    select_box_value = SelectedCurrency.selected_currencies

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
            abbreviation = currency_data.get_abbreviaton()
            from_currency_name = abbreviation.get(from_currency.upper(), "None")
            to_currency_name = abbreviation.get(to_currency.upper(), "None")
            st.success(
                f"{amount} {from_currency_name} is {converted_amount:.2f} {to_currency_name}"
            )
        else:
            st.error("Failed to get the exchange rate.")


if __name__ == "__main__":
    convert_currency()
