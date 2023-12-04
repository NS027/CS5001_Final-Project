import streamlit as st
import requests

# Create a Streamlit input field for the country code
country_code = st.text_input("Enter the country code:")

if country_code:
    # Use an f-string to construct the URL with the provided country code
    url = f"https://flagsapi.com/{country_code}/flat/64.png"

    response = requests.get(url)
    if response.status_code == 200:
        with open("flag.png", "wb") as f:
            f.write(response.content)

        # Display the flag image
        st.image("flag.png")
    else:
        st.write("Flag not found for the provided country code.")
