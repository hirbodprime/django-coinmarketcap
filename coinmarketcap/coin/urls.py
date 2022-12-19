from django.urls import path
from . import views as v
urlpatterns = [
    
    path('scrape-coins/' , v.scrape_coins_view , name="scrape_coins"),
    path('get-coins/' , v.get_coins_view , name="get_coins"),
    path('get-coin/<str:symbol>' , v.get_single_coin_view , name="get_single_coin"),
    path('download-logo/<str:symbol>' , v.download_logo_symbol_view,name="dow_logo"),
    path('get-logo/<str:symbol>' , v.get_logo_symbol_view , name="get_logo"),
    
    
]