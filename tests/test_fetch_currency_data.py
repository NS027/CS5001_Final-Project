"""
Final Project

This file contains the unit test for the class CurrencyData.
"""
import unittest
import requests
from datetime import datetime
from unittest.mock import patch
from models.fetch_currency_data import CurrencyData


class TestCurrencyData(unittest.TestCase):
    def setUp(self):
        self.currency_data = CurrencyData()

    def test_fetch_data_success(self):
        test_url = "https://example.com/api"
        with patch("requests.get") as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {"data": "test data"}

            currency_data = CurrencyData()
            result = currency_data.fetch_data(test_url)
            self.assertEqual(result, {"data": "test data"})

    def test_fetch_data_server_error(self):
        test_url = "https://example.com/api"
        with patch("requests.get") as mock_get:
            mock_get.return_value.status_code = 500

            currency_data = CurrencyData()
            result = currency_data.fetch_data(test_url)
            self.assertIsNone(result)

    def test_fetch_data_request_exception(self):
        test_url = "https://example.com/api"
        with patch("requests.get") as mock_get:
            mock_get.side_effect = requests.exceptions.ConnectionError()

            currency_data = CurrencyData()
            result = currency_data.fetch_data(test_url)
            self.assertIsNone(result)

    def test_get_abbreviation_success(self):
        with patch(
            "models.fetch_currency_data.CurrencyData.fetch_data"
        ) as mock_fetch_data:
            # Set up the mock JSON response to match what the real API returns
            mock_response = {"usd": "US Dollar"}
            mock_fetch_data.return_value = mock_response

            # Invoke the method under test
            result = self.currency_data.get_abbreviation()

            # Convert keys to uppercase to match the method behavior
            expected_result = {
                key.upper(): value for key, value in mock_response.items()
            }

            # Assert that the result matches the mock JSON response
            self.assertEqual(result, expected_result)

    def test_get_abbreviation_failure(self):
        with patch(
            "models.fetch_currency_data.CurrencyData.fetch_data"
        ) as mock_fetch_data:
            mock_fetch_data.return_value = None  # Simulate a failed request

            result = self.currency_data.get_abbreviation()
            self.assertIsNone(result)

    def test_get_exchange_rate_success(self):
        with patch(
            "models.fetch_currency_data.CurrencyData.fetch_data"
        ) as mock_fetch_data:
            mock_response = {"eur": 0.85}
            mock_fetch_data.return_value = mock_response

            result = self.currency_data.get_exchange_rate("usd", "eur")
            self.assertEqual(result, 0.85)

    def test_get_exchange_rate_failure(self):
        with patch(
            "models.fetch_currency_data.CurrencyData.fetch_data"
        ) as mock_fetch_data:
            mock_fetch_data.return_value = None

            result = self.currency_data.get_exchange_rate("usd", "eur")
            self.assertIsNone(result)

    def test_get_currency_from_base_currency_success(self):
        with patch(
            "models.fetch_currency_data.CurrencyData.fetch_data"
        ) as mock_fetch_data:
            # Adjust the mock response to match the expected structure in the method
            mock_response = {"date": "2023-11-28", "cad": {"cny": 5.24}}
            mock_fetch_data.return_value = mock_response

            result = self.currency_data.get_currency_from_base_currency("cad")
            self.assertEqual(result, {"cny": 5.24})

    def test_get_currency_from_base_currency_failure(self):
        with patch(
            "models.fetch_currency_data.CurrencyData.fetch_data"
        ) as mock_fetch_data:
            mock_fetch_data.return_value = None

            result = self.currency_data.get_currency_from_base_currency("eur")
            self.assertIsNone(result)

    def test_get_currency_historical_data_success(self):
        with patch(
            "models.fetch_currency_data.CurrencyData.fetch_data"
        ) as mock_fetch_data:
            mock_response = {"eur": 0.85}
            mock_fetch_data.return_value = mock_response

            result = self.currency_data.get_currency_historical_data(
                "usd", "eur", datetime.strptime("2021-01-01", "%Y-%m-%d")
            )
            self.assertEqual(result, 0.85)

    def test_get_currency_historical_data_failure(self):
        with patch(
            "models.fetch_currency_data.CurrencyData.fetch_data"
        ) as mock_fetch_data:
            mock_fetch_data.return_value = None

            result = self.currency_data.get_currency_historical_data(
                "usd", "eur", datetime.strptime("2021-01-01", "%Y-%m-%d")
            )
            self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
