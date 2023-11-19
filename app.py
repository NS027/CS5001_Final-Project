import streamlit as st
import requests


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
    from_currency = st.selectbox(
        "From currency", ["USD", "CNY", "GBP", "CAD", "EUR"]
    ).lower()
    to_currency = st.selectbox(
        "To currency", ["USD", "CNY", "GBP", "CAD", "EUR"]
    ).lower()

    if st.button("Convert"):
        # Call function to perform conversion (to be implemented)
        result = convert_currency(amount, from_currency, to_currency)
        st.success(
            f"{amount} {from_currency.upper()} is {result:.2f} {to_currency.upper()}"
        )


if __name__ == "__main__":
    main()
