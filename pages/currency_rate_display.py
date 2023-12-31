"""
Final Project

This file contains the function that displays the currency rate.
"""
import streamlit as st
import pandas as pd
from models.selected_currency import SelectedCurrency
from models.fetch_currency_data import CurrencyData


def display_currency_rate():
    """
    Function -- display_currency_rate
        Display the currency rate
    Parameters:
        None
    Returns:
        None
    """

    # Set the page title
    st.markdown(
        '<p style="font-family: Georgia; color:#025167; font-size: 36px; font-weight: bold;">Currency Rate Display</p>',
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
        '<p style="font-family:Georgia; text-align: justify; color:#ARRGGBB; font-size: 15px; font-weight: normal;">Stay updated with our Currency Rate Display, offering real-time visibility into the latest exchange rates, essential for informed financial decision-making.</p>',
        unsafe_allow_html=True,
    )

    # Create an instance of CurrencyData
    currency_data = CurrencyData()

    # Create an instance of SelectedCurrency
    selected_currency = SelectedCurrency()

    # Set the select box value
    select_box_value = selected_currency.get_selected_currencies()

    # Set the base currency to a select box in streamlit
    base_currency = st.selectbox("Base currency", select_box_value)

    # Using pandas to convert the dictionary to a dataframe
    new_dict = currency_data.get_currency_from_base_currency(base_currency)
    df = pd.DataFrame.from_dict(new_dict, orient="index")

    # Rename the second column to "Rate"
    df = df.rename(columns={0: "Rate"})
    # Reset the index
    df = df.reset_index()
    # Rename the index column to "Currency"
    df = df.rename(columns={"index": "Currency"})

    # Convert the "Currency" column to uppercase
    df["Currency"] = df["Currency"].str.upper()

    # Filter the dataframe to only show the selected cureencies
    df = df[df["Currency"].isin(select_box_value)]
    # Remove the base currency from the dataframe
    df = df[df["Currency"] != base_currency]

    # Sort the dataframe by the "Currency" column
    df = df.reset_index(drop=True)

    # Convert the "Rate" column to float with 2 decimal places
    df["Rate"] = df["Rate"].astype(float).round(2)

    # Calaculate the buy rate
    df["Buy Rate"] = (1 / df["Rate"]).round(2)

    # # Display the dataframe without the index column
    # st.dataframe(df.set_index("Currency"))

    # Create the DataFrame
    df = pd.DataFrame(
        {
            "Currency": df["Currency"],
            "Rate": df["Rate"],
            "Buy Rate": df["Buy Rate"],
        }
    )

    # Define the styles for table headers and data cells
    s1 = dict(selector="th", props=[("text-align", "center")])
    s2 = dict(selector="td", props=[("text-align", "center")])

    # Create the Styler object and apply the formatting
    styler = df.style.set_table_styles([s1, s2]).hide(axis=0)
    styler = styler.format({"Rate": "{:.2f}", "Buy Rate": "{:.2f}"})
    df_html = styler.to_html(escape=False)  # Convert DataFrame to HTML with styles

    # Use columns to control the layout
    col1, col2, col3 = st.columns([2, 3, 1])
    with col2:
        st.write(df_html, unsafe_allow_html=True)


if __name__ == "__main__":
    display_currency_rate()
