"""
Final Project

This file contains the driver function that runs the program.
"""
import streamlit as st
from helper import display_link
from st_pages import Page, show_pages, add_page_title


def main_page():
    """
    Function -- main_page
        Display the main page
    Parameters:
        None
    Returns:
        None
    """
    # Set the page title
    st.markdown(
        '<p style="font-family: Georgia; color:#025167; font-size: 36px; font-weight: bold;">Currency Compass</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <style>
        .justify-text {
            text-align: justify;
            font-family: Helvetica;
            color: #ARRGGBB;
            font-size: 14px;
            font-weight: normal;
        }
        </style>
        <p class="justify-text">Welcome to Currency Compass, your essential guide in the dynamic world of currencies. 
        Our platform provides real-time currency conversion, current exchange rates, historical data analysis, and trend-tracking line charts. 
        Designed for investors, travelers, and financial enthusiasts alike, Currency Compass offers accurate, timely information and an intuitive interface for all your currency-related needs. 
        Navigate the complexities of global finance with ease and confidence, as we bring financial clarity and insights right to your fingertips.</p>
        """,
        unsafe_allow_html=True,
    )

    # Add a divider
    st.markdown(
        """
    <div style='height: 3px; background-color: #3A3B3C; margin-top: 5px; margin-bottom: 3px;'></div>
    <div style='height: 2px; background-color: #3A3B3C; margin-top: 3px; margin-bottom: 5px;'></div>
    """,
        unsafe_allow_html=True,
    )

    # Create two columns for the features
    col1, col2 = st.columns(2)

    with col1:
        # Set the Currency Converter title
        st.markdown(
            '<p style="font-family:Georgia; color:#025167; font-size: 20px; font-weight: bold;">💱Currency Convertor</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style="font-family:Helvetica; text-align: justify; color:#ARRGGBB; font-size: 14px; font-weight: normal;">Experience instant currency conversion with real-time accuracy, ensuring you get the most up-to-date exchange rates at the click of a button.</p>',
            unsafe_allow_html=True,
        )

        # Create a hyperlink for the Currency Converter
        display_link("/Currency Converter", ":orange[**Click Here**]")
    with col2:
        # Set the Currency Rate Display title
        st.markdown(
            '<p style="font-family:Georgia; color:#025167; font-size: 20px; font-weight: bold;">📊Rate Display</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style="font-family:Helvetica; text-align: justify; color:#ARRGGBB; font-size: 14px; font-weight: normal;">Stay informed with the latest exchange rates, providing you with the pulse of the currency markets for informed financial decisions.</p>',
            unsafe_allow_html=True,
        )

        # Create a hyperlink for the Currency Converter
        display_link("/Currency Rate Display", ":orange[**Click Here**]")

    # Create columns for the features
    col3, col4 = st.columns(2)
    with col3:
        # Set the Currency Historical Rate title
        st.markdown(
            '<p style="font-family:Georgia; color:#025167; font-size: 20px; font-weight: bold;">🕒Historical Rate</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style="font-family:Helvetica; text-align: justify; color:#ARRGGBB; font-size: 14px; font-weight: normal;">Analyze historical data to gain insights into the currency markets, and track trends to make informed decisions.</p>',
            unsafe_allow_html=True,
        )

        # Create a hyperlink for the Currency Converter
        display_link("/Currency Historical Rate", ":orange[**Click Here**]")
    with col4:
        # Set the Currency Line Chart title
        st.markdown(
            '<p style="font-family:Georgia; color:#025167; font-size: 20px; font-weight: bold;">📈Line Chart</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style="font-family:Helvetica; text-align: justify; color:#ARRGGBB; font-size: 14px; font-weight: normal;">Track trends with our line charts, providing you with a visual representation of the currency markets.</p>',
            unsafe_allow_html=True,
        )

        # Create a hyperlink for the Currency Converter
        display_link("/Currency Line Chart", ":orange[**Click Here**]")

    # Set the Currency Comprehensive Display title
    st.markdown(
        '<p style="font-family:Georgia; color:#025167; font-size: 20px; font-weight: bold;">🌐Comprehensive Display</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p style="font-family:Helvetica; text-align: justify; color:#ARRGGBB; font-size: 14px; font-weight: normal;">Explore market dynamics with our Comprehensive Rate Display, which encapsulates rate trends and current exchange rates at a glance. Secure the best deals with up-to-date buy rates, ensuring you are well-informed for your currency transactions.</p>',
        unsafe_allow_html=True,
    )
    # Create a hyperlink for the Currency Converter
    display_link("/Currency Comprehensive Display", ":orange[**Click Here**]")

    # Add a divider
    st.markdown(
        """
    <div style='height: 2px; background-color: #3A3B3C; margin-top: 5px; margin-bottom: 5px;'></div>
    <div style='height: 3px; background-color: #3A3B3C; margin-top: 3px; margin-bottom: 5px;'></div>
    """,
        unsafe_allow_html=True,
    )


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
            "Currency Comprehensive Display", "🌐"),
    ]

    show_pages(pages)
    # display_link("/", "Home")


if __name__ == "__main__":
    main_page()
    main()
