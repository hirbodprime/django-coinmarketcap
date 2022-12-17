from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpRequest ,JsonResponse
from coinmarketcapscraper.coinsmarketcap import Scraper
from .models import CoinDataModel 
import os
import tempfile
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


def save_image_from_url(req, symbol):
    get_coin = Scraper(download_all_logos=False , coin_data=True,coin_data_file=False,download_logo_sybmol=symbol)
    src_symbol = get_coin.download_logo_symbol()
    coin = CoinDataModel.objects.get(symbol=symbol)
    logo_url = src_symbol[0]
    logo_symbol = src_symbol[1]
    image_content = src_symbol[2]
    img_temp = NamedTemporaryFile()
    print(img_temp)
    img_temp.write(image_content.content)
    img_temp.flush()
    if not coin.image:
        coin.image.save(f"logo-{symbol}.jpg", File(img_temp), save=True)
    return render(req,"single_coin_logo.html",{"coin":coin})

def download_logo_symbol(req,symbol):
    if CoinDataModel.objects.filter(symbol=symbol):
        get_coin = Scraper(download_all_logos=False , coin_data=True,coin_data_file=False,download_logo_sybmol=symbol)
        src_symbol = get_coin.download_logo_symbol()
        logo_url = src_symbol[0]
        logo_symbol = src_symbol[1]

        return HttpResponse("src_symbol")
    else:
        return HttpResponse("send a bad symbol")

def ScrapeCoinmarkepcapView(req):
    get_coin = Scraper(download_all_logos=False , coin_data=True,coin_data_file=False)
    coin_data = get_coin.get_coin_data()

    for c in range(len(coin_data)):
        name = coin_data[c]['name']
        symbol = coin_data[c]['symbol']
        price = coin_data[c]['price']
        CoinDataModel.objects.create(name=name , symbol=symbol,price=price)
    return HttpResponse("coin data Created!")

def JsonDataCoinmarkepcapView(request):
    content_type = request.META.get('HTTP_ACCEPT', request.META.get('CONTENT_TYPE', 'application/your_default'))
    if content_type == "application/xhtml+xml":
        data = CoinDataModel.objects.all()
        return render(request,"coindata.html" , {"coin":data})
    # if content_type == "application/json":
    else:    
        data = list(CoinDataModel.objects.values())
        return JsonResponse(data,safe = False)


def GetCoinData(req,symbol):
    model = list(CoinDataModel.objects.filter(symbol=symbol).values())
    return JsonResponse(model,safe = False)