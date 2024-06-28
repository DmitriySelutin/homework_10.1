import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"


def get_conversion(transactions):
    """Функция конвертации валюты в рубли"""
    amount = transactions["operationAmount"]["amount"]
    currency = transactions["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    elif currency == "USD" or currency == "EUR":
        try:
            response = requests.get(
                API_URL.format(to="RUB", from_=currency, amount=amount), headers={"apikey": API_KEY}
            )
            if response.status_code == 200:
                data = response.json()
                return data["result"]
            else:
                print(f"Ошибка при конвертации валюты: {response.status_code}")
                return 0.0
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при конвертации валюты: {e}")
            return 0.0
    else:
        return 0.0
