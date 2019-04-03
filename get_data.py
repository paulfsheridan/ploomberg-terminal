import json
import requests
import pandas

base_url = "https://cloud.iexapis.com/beta/"
request_types = {"stock":"stock/"}
token = "?token=pk_6eced46aefd9454ba28ae6e64895bcba"
quote = "/quote"

def get_stock_data(symbol):
    live_response = requests.Session()
    response = live_response.get(base_url+request_types["stock"]+symbol+quote+token)
    data = json.loads(response.text)
    return data


def company_name():
    get_stock_data(symbol)

print(get_stock_data("AAPL"))

