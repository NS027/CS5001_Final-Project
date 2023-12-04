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

LINE_CHART_DAYS = 10  # The number of days to display in the line chart


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

    st.title("Currency Comprehensive Display")
    st.write(
        "This page displays the comprehensive currency rate. You can select the currency and the time period."
    )
    select_box_value = selected_currency.get_selected_currencies()
    from_currency = st.selectbox("Select base currency", select_box_value)

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

    # Display the DataFrame without the index
    df = pd.DataFrame(all_data)
    html = df.to_html(escape=False, index=False)  # Convert DataFrame to HTML
    st.markdown(html, unsafe_allow_html=True)


if __name__ == "__main__":
    currency_comprehensive_display()
