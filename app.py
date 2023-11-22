import streamlit as st
import requests

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
    # API endpoint URL
    url = (
        f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Remove the first data from the json
        first_key = list(data.keys())[0]
        del data[first_key]
        # Convert the data into a dictionary
        data = {key.upper(): value for key, value in data.items()}

        return data

    else:
        print(f"Error fetching data: HTTP Status Code {response.status_code}")
        data = None


def convert_currency(amount, from_currency, to_currency):
    # API endpoint URL
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{from_currency}/{to_currency}.json"

    try:
        # Send a request to the API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON
            data = response.json()
            # Get the exchange rate
            exchange_rate = data[to_currency]
            # Perform the conversion
            converted_amount = amount * exchange_rate
            return converted_amount
        else:
            # Handle request errors
            st.error(f"Error fetching data: HTTP Status Code {response.status_code}")
            return None
    except Exception as e:
        # Handle other errors (e.g., network issues)
        st.error(f"An error occurred: {str(e)}")
        return None


def main():
    st.title("Currency Compass")

    st.header("Currency Converter")
    amount = st.number_input("Enter the amount: ")

    currency_list = get_abbreviaton()
    select_box_data = [
        key for key in currency_list.keys() if key in selected_currencies
    ]  # Convert keys to uppercase

    from_currency = st.selectbox("From currency", select_box_data)
    to_currency = st.selectbox("To currency", select_box_data)

    # Convert the selected currency codes to lower case for API compatibility
    from_currency = from_currency.lower()
    to_currency = to_currency.lower()

    if st.button("Convert"):
        result = convert_currency(amount, from_currency, to_currency)
        if result is not None:
            st.success(
                f"{amount} {from_currency.upper()} is {result:.2f} {to_currency.upper()}"
            )


if __name__ == "__main__":
    main()
