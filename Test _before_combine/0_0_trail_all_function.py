"""
Mulei Ni
CS5001 Fall 2023
Final Project

This file contains the all functions that want to demonstrate in project.
"""
import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
from datetime import datetime, timedelta
from io import BytesIO

selected_currencies = [
    "CNY",
    "USD",
    "HKD",
    "GBP",
    "AUD",
    "JPY",
    "EUR",
    "CAD",
    "SGD",
    "NZD",
    "CHF",
]


def get_abbreviaton():
    """
    Function -- get_abbreviaton
        Get the currency abbreviation from the API
    Parameters:
        None
    Returns:
        A dictionary that contains the currency abbreviation
    """
    # API endpoint URL
    url = (
        f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"
    )

    try:
        # Send a request to the API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Remove the first data from the json
            first_key = list(data.keys())[0]
            del data[first_key]
            # Convert the data into a dictionary
            data = {key.upper(): value for key, value in data.items()}

            return data
        else:
            # Handle request errors
            st.error(f"Error fetching data: HTTP Status Code {response.status_code}")
            return None

    except Exception as ex:
        # Handle exceptions
        st.error(f"An error occurred: {ex}")
        return None


def get_exchange_rate(from_currency, to_currency):
    """
    Function -- get_exchange_rate
        Get the exchange rate from the API
    Parameters:
        from_currency -- the currency that the user want to convert from
        to_currency -- the currency that the user want to convert to
    Returns:
        A float that contains the exchange rate
    """
    # API endpointr URL
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{from_currency}/{to_currency}.json"

    try:
        # Send a request to the API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Get the exchange rate
            exchange_rate = data[to_currency]

            return exchange_rate
        else:
            # Handle request errors
            st.error(f"Error fetching data: HTTP Status Code {response.status_code}")
            return None
    except Exception as ex:
        # Handle other errors (e.g., network issues)
        st.error(f"An error occurred: {ex}")
        return None


def get_currency_from_base_currency(base_currency):
    """
    Function -- get_currency_from_base_currency
        Get the currency rate data base on base_currency from the API
    Parameters:
        base_currency -- the currency that the user want to convert from
    Returns:
        A dataframe that contains the currency buy rate data
    """
    # API endpoint API
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{base_currency.lower()}.json"

    try:
        # Send a request to the API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Remove the first data from the json
            first_key = list(data.keys())[0]
            del data[first_key]
            # Create a new dictionary with the keys and values
            new_dict = data[base_currency.lower()]
            return new_dict
        else:
            # Handle request errors
            st.error(f"Error fetching data: HTTP Status Code {response.status_code}")
            return None
    except Exception as ex:
        # Handle other errors (e.g., network issues)
        st.error(f"An error occurred: {ex}")
        return None


def get_currency_historical_data(base_currency, target_currency, days_to_fetch):
    """
    Function -- get_currency_historical_data
        Get the historical currency rate data from the API
    Parameters:
        base_currency -- the currency that the user want to convert from
        target_currency -- the currency that the user want to convert to
        days_to_fetch -- the number of days to fetch
    Returns:
        A list that contains the historical currency rate data
    """
    # # Initialize the days_to_fetch to 0
    # days_to_fetch = 0
    formatted_date = days_to_fetch.strftime("%Y-%m-%d")

    # API endpoint URL
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{formatted_date}/currencies/{base_currency.lower()}/{target_currency.lower()}.json"

    try:
        # Send a request to the API
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            return response.json().get(target_currency.lower())
        else:
            # Handle request errors
            st.error(f"Error fetching data: HTTP Status Code {response.status_code}")
            return None
    except Exception as ex:
        # Handle other errors (e.g., network issues)
        st.error(f"An error occurred: {ex}")
        return None


def main():
    """
    **This is a convertor that convert the currency from one to another**
    """
    amount = st.number_input("Enter the amount: ")
    select_box_data = selected_currencies
    select_from_currency = st.selectbox("From currency", select_box_data)
    select_to_currency = st.selectbox("To currency", select_box_data)

    from_currency = select_from_currency.lower()
    to_currency = select_to_currency.lower()

    abbreviation = get_abbreviaton()
    from_currency_name = abbreviation.get(select_from_currency, "None")
    to_currency_name = abbreviation.get(select_to_currency, "None")
    exchange_rate = get_exchange_rate(from_currency, to_currency)

    if st.button("Convert"):
        result = amount * exchange_rate
        if result is not None:
            st.success(
                f"{amount} {from_currency_name} is {result:.2f} {to_currency_name}"
            )

    """
    **This is a currency rate display that display the currency rate**
    """
    # Set the base currency to a select box in streamlit
    base_currency = st.selectbox("Select base currency", selected_currencies)

    # Using pandas to convert the dictionary into a dataframe
    new_dict = get_currency_from_base_currency(base_currency)
    df = pd.DataFrame.from_dict(new_dict, orient="index")
    # Rename the second column to "Rate"
    df = df.rename(columns={0: "Rate"})
    # Reset the index
    df = df.reset_index()
    # Rename the index column to "Currency"
    df = df.rename(columns={"index": "Currency"})
    # Convert the "Currency" column to uppercase
    df["Currency"] = df["Currency"].str.upper()
    # Filter the dataframe by the selected currencies
    df = df[df["Currency"].isin(selected_currencies)]
    # Reset the index again and align the index
    df = df.reset_index(drop=True)
    # Convert the "Rate" column to float
    df["Rate"] = df["Rate"].astype(float)

    # Remove the selected currency from display
    df = df[df["Currency"] != base_currency]

    # Create the new column of  buy rate and round 2 decimals
    df["Buy Rate"] = (1 / df["Rate"]).round(2)

    # Reorder the columns for display
    df = df[["Currency", "Rate", "Buy Rate"]]

    # Display the DataFrame without the index
    st.dataframe(df.set_index("Currency"))

    """
    **This is a historical currency rate display that display the historical currency rate**
    """
    # Select base currency
    base_currency = st.selectbox("Select base currency", selected_currencies, key=0)
    # Select target currency
    target_currency = st.selectbox("Select target currency", selected_currencies, key=1)

    # Initialize the days_to_fetch to 0
    days_to_fetch = 0

    # Buttons for selecting time frame
    if st.button("1 Days"):
        days_to_fetch = 1
    elif st.button("3 Days"):
        days_to_fetch = 3
    elif st.button("5 Days"):
        days_to_fetch = 5
    elif st.button("15 Days"):
        days_to_fetch = 15

    # Fetch data for the past days
    data = []
    for i in range(days_to_fetch):
        date = datetime.now() - timedelta(days=i)
        rate = get_currency_historical_data(base_currency, target_currency, date)
        if rate is not None:
            data.append({"date": date.strftime("%Y-%m-%d"), "rate": rate})

    # Convert to DataFrame
    df2 = pd.DataFrame(data)
    # Display the Dataframe
    st.write(df2)

    """
    **This is for line chart testing**
    """
    if not df2.empty:
        df2["date"] = pd.to_datetime(df2["date"])
        df2 = df2.sort_values(by="date")

        y_min = df2["rate"].min() * 0.99  # 1% margin at the bottom
        y_max = df2["rate"].max() * 1.01  # 1% margin at the top
        plt.figure(figsize=(10, 6))
        # Plot the exchange rate
        plt.plot(
            df2["date"],
            df2["rate"],
            color="black",
            marker="",
            linestyle="solid",
            linewidth=2,
            markersize=6,
        )
        plt.ylim(y_min, y_max)
        plt.title(f"Exchange rate trend from {base_currency} to {target_currency}")
        plt.xlabel("Date")
        plt.ylabel("Exchange rate")
        plt.xticks(rotation=45)
        plt.grid(False)
        plt.tight_layout()
        st.pyplot(plt)

    """
    **This is for mini chart testing**
    """
    # Select base currency
    from_currency = st.selectbox("Select base currency", selected_currencies, key=2)

    all_data = []
    for to_currency in selected_currencies:
        if to_currency != from_currency:
            # Fetch current rate
            current_rate = get_exchange_rate(from_currency.lower(), to_currency.lower())

            # Ensure current_rate is not None and not zero
            buy_rate = 1 / float(current_rate) if current_rate else None

            # Fetch historical data for mini chart
            historical_data = []
            for i in range(5):
                date1 = datetime.now() - timedelta(days=i)
                rate1 = get_currency_historical_data(
                    from_currency.lower(), to_currency.lower(), date1
                )
                if rate1 is not None:
                    historical_data.append(
                        {"date": date1.strftime("%Y-%m-%d"), "rate": rate1}
                    )

            # Check if historical data is not empty before plotting
            if historical_data:
                df_historical = pd.DataFrame(historical_data)
                df_historical["date"] = pd.to_datetime(df_historical["date"])

                # Mini chart
                plt.figure(figsize=(2, 1))
                plt.plot(df_historical["date"], df_historical["rate"])
                plt.xticks([])
                plt.yticks([])
                plt.tight_layout()
                buf = BytesIO()
                plt.savefig(buf, format="png")
                plt.close()
                mini_chart = base64.b64encode(buf.getvalue()).decode()
            else:
                mini_chart = None

            # Append data
            all_data.append(
                {
                    "Currency": to_currency,
                    "Rate trend": f'<img src="data:image/png;base64,{mini_chart}"/>'
                    if mini_chart
                    else "",
                    "Rate": current_rate,
                    "Buy Rate": buy_rate,
                }
            )

    # Display the DataFrame without the index
    df3 = pd.DataFrame(all_data)
    html = df3.to_html(escape=False, index=False)  # Convert DataFrame to HTML
    st.markdown(html, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
