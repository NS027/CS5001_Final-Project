import streamlit as st
import requests
import pandas as pd

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

# Set the base currency to a select box in streamlit
base_currency = st.selectbox("Select base currency", selected_currencies)

url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{base_currency.lower()}.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Remove the first data from the json
    first_key = list(data.keys())[0]
    del data[first_key]
    # Create a new dictionary with the keys and values in original dictionary's values
    # chosen_currency = base_currency.lower()
    # new_dict = data[chosen_currency]
    new_dict = data[base_currency.lower()]
    # Using pandas to convert the dictionary into a dataframe
    df = pd.DataFrame.from_dict(new_dict, orient="index")
    # Rename the column name first column to 'Currency' second column to "Rate"
    df = df.rename(columns={0: "Rate"})
    # Reset the index
    df = df.reset_index()
    # Rename the index column to "Currency"
    df = df.rename(columns={"index": "Currency"})
    # Convert the "Currency" column to uppercase
    df["Currency"] = df["Currency"].str.upper()
    # Filter the dataframe by the selected currencies
    df = df[df["Currency"].isin(selected_currencies)]
    # Reset the index again
    df = df.reset_index(drop=True)
    # Convert the "Rate" column to float
    df["Rate"] = df["Rate"].astype(float)
    # Display the dataframe
    st.write(df)
