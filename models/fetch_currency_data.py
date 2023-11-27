"""
Final Project

This file contains the function that fetches the currency data from the API.
"""
import requests
import streamlit as st


class CurrencyData:
    """
    Class -- CurrencyData
        This class contains the functions that fetches the currency data from the API.
    Attributes:
        None
    Methods:
        get_abbreviaton -- Get the currency abbreviation from the API
        get_exchange_rate -- Get the exchange rate from the API
        get_currency_from_base_currency -- Get the currency rate data base on base_currency from the API
        get_currency_historical_data -- Get the historical currency rate data from the API
    """

    def __init__(self):
        """
        Initialize CurrencyData with the API base URL
        """
        self.abbreviation = None
        self.exchange_rate = None
        self.base_data = None
        self.historical_data = None

    def fetch_data(self, url):
        """
        Functions -- fetch_data
            Fetch the currency data from the API
        """
        try:
            # Send a reuquest to the API
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                # Handle request errors
                st.error(f"Error fetching data: HTTP Status Code{requests.status_code}")
                return None
        except Exception as ex:
            st.error(f"An error occurred: {ex}")
            return None

    def get_abbreviaton(self):
        """
        Function -- get_abbreviation
            Get the currency abbreviation from the API
        Parameters:
            None
        Returns:
            A dictionary that contains the currency abbreviation
        """
        # API endpoint URL
        url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"

        self.abbreviation = self.fetch_data(url)
        data = self.abbreviation
        # Remove the first data from the json
        first_key = list(data.keys())[0]
        del data[first_key]

        # Convert the data into a dictionary
        self.abbreviation = {key.upper(): value for key, value in data.items()}
        return self.abbreviation

    def get_exchange_rate(self, from_currency, to_currency):
        """
        Function -- get_exchange_rate
           Get the exchange rate from the API
        Parameters:
            from_currency -- the currency that the user want to convert from
            to_currency -- the currency that the user want to convert to
        Returns:
            A float that contains the exchange rate
        """
        # API endpoint URL
        url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{from_currency}/{to_currency}.json"

        data = self.fetch_data(url)
        # Get the exchange rate
        self.exchange_rate = data[to_currency]
        return self.exchange_rate

    def get_currency_from_base_currency(self, base_currency):
        """
        Fuction -- get_currency_from_base_currency
            Get the currency rate data base on base_currency from the API
        Parameters:
            base_currency -- the currency that the user want to convert from
        Returns:
            A dataframe that contains the currency buy rate data
        """
        # API endpoint URL
        url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{base_currency.lower()}.json"

        data = self.fetch_data(url)
        # Remove the first data from the json
        first_key = list(data.keys())[0]
        del data[first_key]
        # Create a new dictionary with the keys and values
        self.base_data = data[base_currency.lower()]
        return self.base_data

    def get_currency_historical_data(self, base_currency, target_currency, date):
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

        formatted_date = date.strftime("%Y-%m-%d")

        # API endpoint URL
        url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{formatted_date}/currencies/{base_currency.lower()}/{target_currency.lower()}.json"

        data = self.fetch_data(url)
        historical_rate = data.get(target_currency.lower())
        return historical_rate
