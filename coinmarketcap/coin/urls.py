from django.urls import path
from . import views as v

urlpatterns = [

    path('api/get-coins/' , v.CoinsListApiView.as_view() , name="get_coins_api"),
    path('api/get-coin/<str:name_or_symbol>' , v.CoinsSearchApiView.as_view() , name="get_single_coin_search_api"),
    path('scrape-coins/' , v.scrape_coins_view , name="scrape_coins"),
    path('get-coins/' , v.get_coins_view , name="get_coins"),
    path('get-coin/<str:symbol_or_name>' , v.get_single_coin_view , name="get_single_coin"),
    path('get-logo/<str:symbol>' , v.download_logo_symbol_view,name="dow_logo"),
    path('get-logos/' , v.download_all_logos,name="dow_logos"),


]
