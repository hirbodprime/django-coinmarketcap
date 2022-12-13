from django.shortcuts import render
from django.http import HttpResponse , HttpRequest ,JsonResponse
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

def JsonDataCoinmarkepcapView(request):
    content_type = request.META.get('HTTP_ACCEPT', request.META.get('CONTENT_TYPE', 'application/your_default'))
    if content_type == "application/xhtml+xml":
        data = CoinDataModel.objects.all()
        return render(request,"coindata.html" , {"coin":data})
    if content_type == "application/json":
    # else:    
        data = list(CoinDataModel.objects.values())
        return JsonResponse(data,safe = False)


def GetCoinData(req,symbol):
    model = list(CoinDataModel.objects.filter(symbol=symbol).values())
    return JsonResponse(model,safe = False)