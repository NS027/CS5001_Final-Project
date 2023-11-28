"""
Mulei Ni
CS 5001, Fall 2023
Final Project

This file contains the unit test for the class SelectedCurrency.
"""
import unittest
from models.selected_currency import SelectedCurrency


class TestSelectedCurrency(unittest.TestCase):
    def test_get_selected_currencies(self):
        expected_currencies = [
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
        # Create an instance of SelectedCurrency
        selected_currency = SelectedCurrency()
        result = selected_currency.get_selected_currencies()
        self.assertEqual(result, expected_currencies)


if __name__ == "__main__":
    unittest.main()
