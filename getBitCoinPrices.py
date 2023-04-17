import requests
import os
from dotenv import load_dotenv

load_dotenv()

def GetBitcoinPrices():

    # Code from RapidAPI to call coinranking API

    url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history"

    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"7d"}

    headers = {
        "X-RapidAPI-Key": os.environ.get('rapid-api-key'),
        "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
    }

    response = requests.request('GET', url, headers=headers, params=querystring)

    # Parse the results to json
    json_results = response.json();

    # Get the history data
    history = json_results['data']['history']

    prices = []

    # Add the prices from each data item in history to prices list
    for item in history:
        prices.append(item['price'])
    
    # Create a comma-separated string of the prices
    pricesList = ','.join(prices)

    return pricesList

GetBitcoinPrices();