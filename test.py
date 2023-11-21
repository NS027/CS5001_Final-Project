import requests

url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

else:
    print(f"Error fetching data: HTTP Status Code {response.status_code}")
    data = None

if data:
    first_key = list(data.keys())[0]
    del data[first_key]

    print(data)
