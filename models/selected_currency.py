"""
Final Project

This file contains the selected currency class.
"""


class SelectedCurrency:
    """
    This class contains the selected currencies.
    """

    def __init__(self):
        """
        This function initializes the selected currencies.
        """
        self.selected_currencies = []

    def get_selected_currencies(self):
        """
        This function returns the selected currencies.
        """
        self.selected_currencies = [
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
        return self.selected_currencies
