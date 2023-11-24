"""
Final Project

This file contains the function that converts the currency.
"""
import streamlit as st
from models.selected_currency import SelectedCurrency
from models.fetch_currency_data import get_exchange_rate, get_abbreviaton


def convert_currency(from_currency, to_currency, amount):
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
    # Get the exchange rate from the API
    exchange_rate = get_exchange_rate(from_currency, to_currency)

    # Convert the currency
    converted_amount = amount * exchange_rate

    # Get the currency abbreviation
    abbreviation = get_abbreviaton()
    from_currency_name = abbreviation.get(from_currency.upper(), "None")
    to_currency_name = abbreviation.get(to_currency.upper(), "None")

    # Display the conversion result
    st.success(
        f"{amount} {from_currency_name} is {converted_amount:.2f} {to_currency_name}"
    )

    return converted_amount
