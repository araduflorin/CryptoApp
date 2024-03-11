# coincap_app/views.py
import requests
from django import template
from django.shortcuts import render
from numerize import numerize
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
            'marketCapUsd': coin_data['marketCapUsd'],
            'changePercent24Hr': coin_data['changePercent24Hr'],
            'vwap24Hr': coin_data['vwap24Hr'],
        }
        coins.append(coin)

    return render(request, 'appCrypto/coin_list.html', {'coins': coins})
    # return render(request, 'appCrypto/test.html', {'coins': coins})


def bitcoin_history(request):
    api_url = 'https://api.coincap.io/v2/assets/bitcoin/history?interval=d1'
    response = requests.get(api_url)
    bitcoin_data = response.json()['data']  # Extracting relevant data

    # You may need to process bitcoin_data further depending on the structure of the API response

    return render(request, 'test1.html', {'bitcoin_data': bitcoin_data})

