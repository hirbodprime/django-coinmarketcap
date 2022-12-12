from django.contrib import admin
from .models import CoinDataModel

class CoinDataModelAdmin(admin.ModelAdmin):
    list_display = ['name' , 'id' ,'symbol' ,'price' ]

admin.site.register(CoinDataModel , CoinDataModelAdmin)