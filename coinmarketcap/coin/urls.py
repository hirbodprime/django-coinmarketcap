from django.urls import path
from . import views as v
urlpatterns = [
    
    path('data/' , v.ScrapeCoinmarkepcapView , name="createdata"),
    path('json-data/' , v.JsonDataCoinmarkepcapView),
    path('coin-data/<str:symbol>' , v.GetCoinData),
    path('download-logo/<str:symbol>' , v.save_image_from_url),
    
    
]