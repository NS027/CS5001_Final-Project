"""
Final Project

This file contains the driver function that runs the program.
"""
import streamlit as st
import pandas as pd
from pages.currency_convertor import convert_currency
from models.selected_currency import SelectedCurrency


def main():
    """
    Function -- main
        The driver function that runs the program.
    Parameters:
        None
    Returns:
        None
    """
    # Set the page title and favicon
    st.set_page_config(page_title="Currency Convertor", page_icon="💲")

    # Set the sidebar title
    st.sidebar.title("Currency Convertor")

    # Set the sidebar subtitle
    st.sidebar.subheader("Select a page to view")

    # Get the entered amount from the user
    amount = st.number_input("Enter the amount: ")
    # Set the select box value
    select_box_value = SelectedCurrency.selected_currencies

    # Set the select box
    select_from_currency = st.selectbox("From currency", select_box_value)
    select_to_currency = st.selectbox("To currency", select_box_value)

    from_currency = select_from_currency.lower()
    to_currency = select_to_currency.lower()

    # Call convert_currency with the required arguments
    if st.button("Convert"):
        convert_currency(from_currency, to_currency, amount)


if __name__ == "__main__":
    main()
