from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseNotFound ,JsonResponse,HttpResponseRedirect
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView
from django.db.models import Q
from rest_framework.generics import ListAPIView , RetrieveAPIView
from coinmarketcapscraper.coinsmarketcap import Scraper
from .models import CoinDataModel
from .serializers import CoinsListApiSerializer 
from home.forms import get_single_coin_form
import tempfile
import os


class CoinsSearchApiView(ListAPIView):
    serializer_class = CoinsListApiSerializer    
    def get_queryset(self):
        name_or_symbol = self.kwargs['name_or_symbol']
        return CoinDataModel.objects.filter(
        Q(name__startswith=name_or_symbol) |
        Q(symbol__startswith=name_or_symbol)
    )



class CoinsListApiView(ListAPIView):
    queryset = CoinDataModel.objects.all()
    serializer_class = CoinsListApiSerializer

def download_logo_symbol_view(req,symbol):
    if CoinDataModel.objects.get(symbol=symbol):
        coin = CoinDataModel.objects.get(symbol=symbol)
        if not coin.image:
            get_coin = Scraper(download_all_logos=False , coin_data=True,coin_data_file=False,download_logo_sybmol=symbol)
            src_symbol = get_coin.download_logo_symbol()
            logo_url = src_symbol[0]
            logo_symbol = src_symbol[1]
            image_content = src_symbol[2]
            img_temp = NamedTemporaryFile()
            img_temp.write(image_content.content)
            img_temp.flush()    
            coin.image.save(f"logo-{symbol}.jpg",File(img_temp), save=True)
            img_temp.close()
            if CoinDataModel.objects.get(symbol=logo_symbol):
                coin = CoinDataModel.objects.get(symbol=logo_symbol)
                return render(req,"single-logo.html" , {"coin":coin})
                # return redirect("get_logo",symbol=logo_symbol)
            else:
                messages.add_message(req, messages.SUCCESS, 'please use one of these symbols')
                return redirect("get_coins")
        else:
            return render(req,"single-logo.html" , {"coin":coin})
    else:
        pass


def scrape_coins_view(req):
    get_coin = Scraper(download_all_logos=False , coin_data=True,coin_data_file=False)
    coin_data = get_coin.get_coin_data()
    for c in range(len(coin_data)):
        name = coin_data[c]['name']
        symbol = coin_data[c]['symbol']
        price = coin_data[c]['price']
        CoinDataModel.objects.update_or_create(name=name , symbol=symbol,
        defaults={'price':price})
    messages.add_message(req, messages.SUCCESS, 'coins scraped!')
    return redirect("get_coins")


def get_coins_view(request):
    if CoinDataModel.objects.all():
        content_type = request.META.get('HTTP_ACCEPT', request.META.get('CONTENT_TYPE', 'application/your_default'))
        if content_type == "application/json":
            coins = list(CoinDataModel.objects.all().values())
            return JsonResponse(coins,safe = False)
        else:
            coins = CoinDataModel.objects.all()
            return render(request,"coins.html" , {"coins":coins})
    else:
        CoinDataModel.objects.all().delete()
        return redirect("scrape_coins")




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