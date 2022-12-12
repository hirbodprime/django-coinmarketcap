from django.urls import path
from . import views as v
urlpatterns = [
    path('data/' , v.ScrapeCoinmarkepcapView),
    path('json-data/' , v.JsonDataCoinmarkepcapView),
    path('coin-data/<str:symbol>' , v.GetCoinData),
    
    
]