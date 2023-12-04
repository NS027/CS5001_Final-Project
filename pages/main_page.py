import streamlit as st
from helper import display_link


def main_page():
    """
    Function -- main_page
        Display the main page
    Parameters:
        None
    Returns:
        None
    """
    st.write("Welcome to Currency Compass!")
    st.write("This is a web application that can help you to convert currency, "
             "display currency exchange rate, display historical currency exchange rate, "
             "display currency line chart and display comprehensive currency information.")
    st.write("Please choose one of the following options to start:")
    # display_header()
    display_link("/Currency Converter", "Convertor")
    display_link("/Currency Rate Display", "Rate Display")
    display_link("/Currency Historical Rate", "Historical Rate")
    display_link("/Currency Line Chart", "Line Chart")
    display_link("/Currency Comprehensive Display", "Comprehensive Display")


if __name__ == "__main__":
    main_page()
