"""
Final Project

This file contains the function that fetches the currency data from the API.
"""
import requests
import streamlit as st


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
