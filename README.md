# Project Summary
This application is designed to cater to the needs of international students and global financial enthusiasts by providing a comprehensive platform for monitoring and analyzing currency exchange rates. It offers real-time exchange rate information with buy rates, historical data visualization, and comprehensive currency rate displays including rate change trends. The interface is user-friendly, allowing easy navigation through various functionalities.

## Description of the REST API(s)
**Name of the REST API:** Free Currency Rates API

**URL of REST API:** <https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@{apiVersion}/{date}/{endpoint}>

**URL of REST API Documentation:** <https://github.com/fawazahmed0/currency-api#free-currency-rates-api>

### Endpoints:
1. **/currencies**
   - Lists all available currencies in prettified JSON format.
   - Example: `https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json`

2. **/currencies/{currencyCode}**
   - Get the currency list with a specific base currency.
   - Example: `https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur.json`

3. **/currencies/{currencyCode}/{currencyCode}**
   - Get the currency value for one currency to another.
   - Example: `https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/jpy.json`

4. **/currencies/{formattedDate}/{currencyCode}/{currencyCode}**
   - Fetch historical data based on two currencies on specific dates.
   - Example: `https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{formatted_date}/currencies/{base_currency.lower()}/{target_currency.lower()}.json`

### Description
- **/currencies**
  - Fetches available currencies values. Used in currency converter.
- **/currencies/{currencyCode}**
  - Displays currency rate based on base currency. Used in currency rate display.
- **/currencies/{currencyCode}/{currencyCode}**
  - Fetches currency between two specific currencies. Used in currency converter and comprehensive display.
- **/currencies/{formattedDate}/{currencyCode}/{currencyCode}**
  - Fetches historical data for two currencies on specific dates. Used in historical rate, line chart, and comprehensive display.

## List of Features
1. **Currency Converter**
   - Description: Converts currencies and calculates the amount based on user input.
   - Model: CurrencyData
   - Endpoint: `/currencies/{currencyCode}/{currencyCode}`
   - Page: Currency Converter

2. **Currency Rate Display**
   - Description: Displays converting and buy rates based on a base currency.
   - Model: CurrencyData
   - Endpoint: `/currencies/{currencyCode}`
   - Page: Currency Rate Display

3. **Currency Historical Rate**
   - Description: Displays historical rates for a specific date range.
   - Model: CurrencyData
   - Endpoint: `/currencies/{formattedDate}/{currencyCode}/{currencyCode}`
   - Page: Currency Historical Rate

4. **Currency Line Chart**
   - Description: Shows currency rate trends in a line chart for a specific date range.
   - Model: CurrencyData
   - Endpoint: `/currencies/{formattedDate}/{currencyCode}/{currencyCode}`
   - Page: Currency Line Chart

5. **Currency Comprehensive Display**
   - Description: Shows real-time rates, buy rates, and rate trends.
   - Model: CurrencyData
   - Endpoint: `/currencies/{currencyCode}/{currencyCode}`, `/currencies/{formattedDate}/{currencyCode}/{currencyCode}`
   - Page: Currency Comprehensive Display

## References
1. **Pandas Documentation**
   - [Pandas](https://pandas.pydata.org/)
   - [Pandas Documentation](https://pandas.pydata.org/docs/)

2. **Matplotlib Documentation**
   - [Matplotlib](https://matplotlib.org/)
   - [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

3. **BytesIO - io Module**
   - [io — Core tools for working with streams](https://docs.python.org/3/library/io.html#io.BytesIO)

4. **base64 Module**
   - [base64 — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html)



