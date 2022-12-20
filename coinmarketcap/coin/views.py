from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseNotFound ,JsonResponse
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.contrib import messages
from coinmarketcapscraper.coinsmarketcap import Scraper
from .models import CoinDataModel
from .forms import get_single_coin_form
import tempfile
import os


def get_logo_symbol_view(request, symbol):
    try:
        coin = CoinDataModel.objects.get(symbol=symbol)
        print(coin.symbol)
        if coin.image:
            return render(request,"single-logo.html" , {"coin":coin})
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
        return redirect("get_coins")
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
        messages.add_message(req, messages.SUCCESS, 'coins created!')
        return redirect("get_coins")
    except:
        messages.add_message(req, messages.SUCCESS, "coins are already created!")
        return redirect("get_coins")

def get_coins_view(request):
    form = get_single_coin_form(request.POST or None)
    if request.method == "GET":
        content_type = request.META.get('HTTP_ACCEPT', request.META.get('CONTENT_TYPE', 'application/your_default'))
        if content_type == "application/json":
            coins = list(CoinDataModel.objects.all().values())
            return JsonResponse(coins,safe = False)
        else:    
            coins = CoinDataModel.objects.all()
            return render(request,"coins.html" , {"coins":coins,'form':form})
    elif request.method == "POST":
        if form.is_valid():
            symbol_or_name = form.cleaned_data['symbol_or_name']
            print(symbol_or_name)
            return redirect("get_single_coin",symbol_or_name=symbol_or_name)


def get_single_coin_view(request,symbol_or_name):
    
    content_type = request.META.get('HTTP_ACCEPT', request.META.get('CONTENT_TYPE', 'application/your_default'))
    try:
        html_coin = CoinDataModel.objects.get(symbol=symbol_or_name)
        if content_type == "application/json":
            json_coin = list(CoinDataModel.objects.filter(symbol=symbol).values())
            return JsonResponse(json_coin[0],safe = False)
        else:
            return render(request, "coin-detail.html", {"coin": html_coin})
    except CoinDataModel.DoesNotExist:
        try:
            html_coin = CoinDataModel.objects.get(name=symbol_or_name)
            if content_type == "application/json":
                json_coin = list(CoinDataModel.objects.filter(name=symbol_or_name).values())
                return JsonResponse(json_coin[0],safe = False)
            else:
                return render(request, "coin-detail.html", {"coin": html_coin})
        except:
            return HttpResponseNotFound("<h3>404 coin not found!</h3>")