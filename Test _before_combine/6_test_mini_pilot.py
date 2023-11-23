import streamlit as st
import pandas as pd
import requests
from io import BytesIO
import base64
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

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


def fetch_historical_data(base, target, date):
    formatted_date = date.strftime("%Y-%m-%d")
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{formatted_date}/currencies/{base.lower()}/{target.lower()}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get(target.lower())
    return None


def plot_mini_chart(data):
    plt.figure(figsize=(2, 1))  # Small plot
    plt.plot(data["date"], data["rate"])
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    return base64.b64encode(buf.getvalue()).decode()


def main():
    base_currency = st.selectbox("Select base currency", selected_currencies)

    all_data = []
    for currency in selected_currencies:
        if currency != base_currency:
            # Fetch current rate
            url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{base_currency.lower()}/{currency.lower()}.json"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                current_rate = data.get(currency.lower())

                # Ensure current_rate is not None and not zero
                if current_rate:
                    buy_rate = 1 / float(current_rate)
                else:
                    buy_rate = None

                # Fetch historical data for mini chart
                historical_data = []
                for i in range(15):
                    date = datetime.now() - timedelta(days=i)
                    rate = fetch_historical_data(base_currency, currency, date)
                    if rate is not None:
                        historical_data.append(
                            {"date": date.strftime("%Y-%m-%d"), "rate": rate}
                        )
                df_historical = pd.DataFrame(historical_data)
                df_historical["date"] = pd.to_datetime(df_historical["date"])
                mini_chart = plot_mini_chart(df_historical) if historical_data else None

                # Append data
                all_data.append(
                    {
                        "Currency": currency,
                        "Rate Trend": f'<img src="data:image/png;base64,{mini_chart}"/>'
                        if mini_chart
                        else "",
                        "Rate": current_rate,
                        "Buy Rate": buy_rate,
                    }
                )

    df = pd.DataFrame(all_data)
    html = df.to_html(escape=False, index=False)  # Convert DataFrame to HTML
    st.markdown(html, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
