"""
Final Project

This file contains the function that displays the comprehensive currency rate.
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
from datetime import datetime, timedelta
from io import BytesIO
from models.selected_currency import SelectedCurrency
from models.fetch_currency_data import CurrencyData

LINE_CHART_DAYS = 5  # The number of days to display in the line chart


def mini_chart(df_historical):
    """
    Function -- mini_chart
        Generate a mini chart for the currency rate
    Parameters:
        df_historical -- the DataFrame that contains the historical data
    Returns:
        A base64 encoded string that contains the mini chart
    """
    plt.figure(figsize=(2, 1))
    plt.plot(df_historical["date"], df_historical["rate"])
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    return base64.b64encode(buf.getvalue()).decode()


def currency_comprehensive_display():
    """
    Function -- currency_comprehensive_display
        Display the comprehensive currency rate
    Parameters:
        None
    Returns:
        None
    """
    # Create an instance of CurrencyData
    currency_data = CurrencyData()

    # Create an instance of SelectedCurrency
    selected_currency = SelectedCurrency()

    # Set the page title
    st.markdown(
        '<p style="font-family: Georgia; color:#025167; font-size: 36px; font-weight: bold;">Currency Comprehensive Display</p>',
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
        '<p style="font-family:Georgia; text-align: justify; color:#ARRGGBB; font-size: 15px; font-weight: normal;">This page displays the comprehensive currency rate. You can select the currency and the time period.</p>',
        unsafe_allow_html=True,
    )

    select_box_value = selected_currency.get_selected_currencies()
    from_currency = st.selectbox(":orange[**Select base currency**]", select_box_value)

    all_data = []
    for to_currency in select_box_value:
        if to_currency != from_currency:
            current_rate = currency_data.get_exchange_rate(
                from_currency.lower(), to_currency.lower()
            )
            if current_rate:
                # Round the rate to 2 decimal places
                current_rate = round(current_rate, 2)
            else:
                None
            # Calculate the buy rate
            buy_rate = 1 / float(current_rate)
            if buy_rate:
                # Round the buy rate to 2 decimal places
                buy_rate = round(buy_rate, 2)
            else:
                None

            historical_data = []
            for i in range(LINE_CHART_DAYS):
                date = datetime.now() - timedelta(days=i)
                rate = currency_data.get_currency_historical_data(
                    from_currency.lower(), to_currency.lower(), date
                )
                if rate is not None:
                    historical_data.append(
                        {"date": date.strftime("%Y-%m-%d"), "rate": rate}
                    )

            if historical_data:
                # Convert the historical data to DataFrame and generate mini chart
                df_historical = pd.DataFrame(historical_data)
                df_historical["date"] = pd.to_datetime(df_historical["date"])
                chart_img = mini_chart(df_historical)

                chart_html = (
                    f'<img src="data:image/png;base64,{chart_img}"/>'
                    if chart_img
                    else ""
                )

            all_data.append(
                {
                    "Currency": to_currency,
                    "Rate trend": chart_html,
                    "Rate": current_rate,
                    "Buy Rate": buy_rate,
                }
            )

    # Create the DataFrame
    df = pd.DataFrame(all_data)

    # Define the styles for table headers and data cells
    s1 = dict(selector="th", props=[("text-align", "center")])
    s2 = dict(selector="td", props=[("text-align", "center")])

    # Create the Styler object and apply the formatting
    styler = df.style.set_table_styles([s1, s2]).hide(axis=0)
    styler = styler.format({"Rate": "{:.2f}", "Buy Rate": "{:.2f}"})
    df_html = styler.to_html(escape=False)  # Convert DataFrame to HTML with styles

    # Use columns to control the layout
    col1, col2, col3 = st.columns([2, 10, 2])
    with col2:
        st.write(df_html, unsafe_allow_html=True)  # Display the styled table


if __name__ == "__main__":
    currency_comprehensive_display()
