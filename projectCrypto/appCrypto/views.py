# coincap_app/views.py
import requests
from django.shortcuts import render

from projectCrypto.secret_key import value_secret_key


def coin_list(request):
    api_key = value_secret_key
    api_url = 'https://api.coincap.io/v2/assets'

    headers = {'Authorization': api_key}

    response = requests.get(api_url, headers=headers)
    data = response.json()['data']

    # response = requests.get('wss://ws.coincap.io/prices?assets=ALL')
    # data = response.json()['data']

    coins = []
    for coin_data in data:
        coin = {
            'rank': coin_data['rank'],
            'name': coin_data['name'],
            'symbol': coin_data['symbol'],
            # 'icon_url': coin_data['icon'],
            'price_usd': coin_data['priceUsd'],
            'changePercent24Hr': coin_data['changePercent24Hr'],
            'vwap24Hr': coin_data['vwap24Hr'],
        }
        coins.append(coin)

    return render(request, 'appCrypto/coin_list.html', {'coins': coins})
    # return render(request, 'appCrypto/test.html', {'coins': coins})
