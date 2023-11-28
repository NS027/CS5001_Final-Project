"""
Final Project

This file contains the driver function that runs the program.
"""
import streamlit as st
from st_pages import Page, show_pages, add_page_title


def main():
    """
    Function -- main
        The driver function that runs the program.
    Parameters:
        None
    Returns:
        None
    """
    # Set the page title
    add_page_title("Navigation")

    pages = [
        Page("pages/main_page.py", "Home", "🏠"),
        Page("pages/currency_convertor.py", "Currency Converter", "💱"),
        Page("pages/currency_rate_display.py", "Currency Rate Display", "📊"),
        Page("pages/currency_historical_rate.py", "Currency Historical Rate", "🕒"),
        Page("pages/currency_line_chart.py", "Currency Line Chart", "📈"),
        Page(
            "pages/currency_comprehensive_display.py",
            "Currency Comprehensive Display",
            "🌐"),
    ]

    show_pages(pages)


if __name__ == "__main__":
    main()
