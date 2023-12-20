import requests

API_KEY = "fca_live_F4w1EAxASg6GFmGAaqaBbiasSoTX3dz2EJRSz2bv"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "AUD", "EUR", "GBP", "CNY", "JPY", "BGN", "CZK", "DKK", "HUF",
              "PLN", "RON", "SEK", "CHF", "ISK", "NOK", "HRK", "RUB", "TRY", "BRL", "HKD",
              "IDR", "ILS", "INR", "KRW", "MXN", "MYR", "NZD", "PHP", "SGD", "THB", "ZAR"]


def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()['data']
        del data[base]
        return data
    except:
        print("Invalid Currency")
        return None


