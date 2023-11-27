"""
Final Project

This file contains the driver function that runs the program.
"""
import streamlit as st
from pages.main_page import main_page
from pages.currency_convertor_copy import convert_currency
from pages.currency_rate_display_copy import display_currency_rate
from pages.currency_historical_rate_copy import display_historical_currency_rate
from pages.currency_line_chart_copy import currency_line_chart
from pages.currency_comprehensive_display_copy import currency_comprehensive_display


def main():
    """
    Function -- main
        The driver function that runs the program.
    Parameters:
        None
    Returns:
        None
    """
    st.title("Currency Compass")
    # Other elements on the Home page

    # Add the main page to the PAGES dictionary
    PAGES = {
        "Home": main_page,
        "Currency Converter": convert_currency,
        "Currency Rate Display": display_currency_rate,
        "Currency Historical Rate": display_historical_currency_rate,
        "Currency Line Chart": currency_line_chart,
        "Currency Comprehensive Display": currency_comprehensive_display,
    }

    # Use a selectbox for navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    # Call the app function on the selected page
    page_func = PAGES[selection]
    page_func()


if __name__ == "__main__":
    main()
