from django.shortcuts import render , redirect
from django.http import HttpResponse
from coin.forms import get_single_coin_form
def home(request):
    form = get_single_coin_form(request.POST or None)
    if request.method == "GET":
        return render(request, 'home.html', {'form':form})
    elif request.method == "POST":
        if form.is_valid():
            symbol_or_name = form.cleaned_data['symbol_or_name']
            print(symbol_or_name)
            return redirect("get_single_coin",symbol_or_name=symbol_or_name)
    else:
        return redirect('get_coins')