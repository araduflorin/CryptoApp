# coincap_app/views.py
import requests
from django.shortcuts import render



def coin_list(request):
    api_url = 'https://api.coincap.io/v2/assets'
    headers = {'Authorization': 'Bearer 514fca50-c212-41b3-8efd-1db57a2d4cda'}

    # api_icons = 'https://assets.coincap.io/assets/icons/{}@2x.png'

    response = requests.get(api_url, headers=headers)
    data = response.json()['data']

    coins = []
    for coin_data in data:
        coin = {
            'name': coin_data['name'],
            'symbol': coin_data['symbol'],
            # 'icon_url': coin_data['icon'],
            'price_usd': coin_data['priceUsd'],
            'changePercent24Hr': coin_data['changePercent24Hr'],
            'vwap24Hr': coin_data['vwap24Hr'],
        }
        coins.append(coin)

    return render(request, 'appCrypto/coin_list.html', {'coins': coins})
