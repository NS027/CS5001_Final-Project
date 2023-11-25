"""
Final Project

This file contains the driver function that runs the program.
"""
import streamlit as st
from pages.main_page import main_page
from pages.currency_convertor import convert_currency
from pages.currency_rate_display import display_currency_rate


def main():
    """
    Function -- main
        The driver function that runs the program.
    Parameters:
        None
    Returns:
        None
    """
    st.title("Welcome to Currency Compass")
    # Other elements on the main page

    # Add the main page to the PAGES dictionary
    PAGES = {
        "Home": main_page,
        "Currency Converter": convert_currency,
        "Currency Rate Display": display_currency_rate,
        # Add other pages as needed
    }

    # Use a selectbox for navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    # Call the app function on the selected page
    page_func = PAGES[selection]
    page_func()


if __name__ == "__main__":
    main()
