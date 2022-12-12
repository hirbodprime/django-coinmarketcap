from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from coinmarketcapscraper.coinsmarketcap import scraper
from .models import CoinDataModel

app = scraper(downloadlogo=False , coin_data=True,coin_data_file=False)
 

def ScrapeCoinmarkepcapView(req):
    coin_data = app.get_coin_data()

    for c in range(len(coin_data)):
        name = coin_data[c]['name']
        symbol = coin_data[c]['symbol']
        price = coin_data[c]['price']
        CoinDataModel.objects.create(name=name , symbol=symbol,price=price)
    return HttpResponse("hi")

def JsonDataCoinmarkepcapView(req):
    data = list(CoinDataModel.objects.values())
    return JsonResponse(data,safe = False)

def GetCoinData(req,symbol):
    model = list(CoinDataModel.objects.filter(symbol=symbol).values())
    return JsonResponse(model,safe = False)