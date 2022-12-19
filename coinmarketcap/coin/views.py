from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpRequest ,JsonResponse
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.contrib import messages
from coinmarketcapscraper.coinsmarketcap import Scraper
from .models import CoinDataModel
import tempfile
import os


def get_logo_symbol_view(request, symbol):
    try:
        coin = CoinDataModel.objects.get(symbol=symbol)
        if coin.image: 
            return render(request,"singlelogo.html" , {"coin":coin})
        else:
            return redirect("dow_logo" , symbol=coin.symbol)
    except CoinDataModel.DoesNotExist:
        messages.add_message(request, messages.SUCCESS, 'please use one of these symbols')
        return redirect("scrape_coins")

def download_logo_symbol_view(req,symbol):
    try:
            coin = CoinDataModel.objects.get(symbol=symbol)
            get_coin = Scraper(download_all_logos=False , coin_data=True,coin_data_file=False,download_logo_sybmol=symbol)
            src_symbol = get_coin.download_logo_symbol()
            logo_url = src_symbol[0]
            logo_symbol = src_symbol[1]
            image_content = src_symbol[2]
            img_temp = NamedTemporaryFile()
            img_temp.write(image_content.content)
            img_temp.flush()
            if not coin.image:
                coin.image.save(f"logo-{symbol}.jpg",File(img_temp), save=True)
            return redirect("get_logo",symbol=logo_symbol)
    except:
        messages.add_message(req, messages.SUCCESS, 'please use one of these symbols')
        return redirect("scrape_coins")
def scrape_coins_view(req):
    try:
        if CoinDataModel.objects.all():
            raise Exception("coins already exists!")
        get_coin = Scraper(download_all_logos=False , coin_data=True,coin_data_file=False)
        coin_data = get_coin.get_coin_data()
        for c in range(len(coin_data)):
            name = coin_data[c]['name']
            symbol = coin_data[c]['symbol']
            price = coin_data[c]['price']
            CoinDataModel.objects.create(name=name , symbol=symbol,price=price)
        return redirect("get_coins")
    except:
        messages.add_message(req, messages.SUCCESS, "coins are already created!")
        return redirect("get_coins")

def get_coins_view(request):
    content_type = request.META.get('HTTP_ACCEPT', request.META.get('CONTENT_TYPE', 'application/your_default'))
    if content_type == "application/json":
        coins = list(CoinDataModel.objects.all().values())
        return JsonResponse(coins,safe = False)
    else:    
        coins = CoinDataModel.objects.all()
        return render(request,"coindata.html" , {"coins":coins})


def get_single_coin_view(request,symbol):
    content_type = request.META.get('HTTP_ACCEPT', request.META.get('CONTENT_TYPE', 'application/your_default'))
    try:
        html_coin = CoinDataModel.objects.get(symbol=symbol)
        if content_type == "application/json":
            json_coin = list(CoinDataModel.objects.filter(symbol=symbol).values())
            return JsonResponse(json_coin[0],safe = False)
        else:
            return render(request, "coindata.html", {"coin": html_coin})
    except CoinDataModel.DoesNotExist:
        messages.add_message(request, messages.SUCCESS, "please use one of these symbols")
        return redirect("scrape_coins")