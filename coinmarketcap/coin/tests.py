from django.test import TestCase , Client
from .models import CoinDataModel
from django.urls import reverse 
import json

class TestModels(TestCase):
    def setUp(self):
        client = Client()
        self.get_coins = reverse('get_coins')
        self.get_single_coin = reverse('get_single_coin',args=["HPF"])
        self.get_logo = reverse('dow_logo', args=['BTC'])
        self.coins = CoinDataModel.objects.create(
            symbol="HPF",
            name="hashtag poor festival",
            price="$1.923.312.412"
        )
    def test_coins(self):
        self.assertEquals(self.coins.symbol, "HPF")
        self.assertEquals(self.coins.name, "hashtag poor festival")
        self.assertEquals(self.coins.price, "$1.923.312.412")

    def test_logo_symbol(self):
        res = self.client.get(self.get_coins)
        self.assertEquals(res.status_code , 200)
        self.assertTemplateUsed(res,"coindata.html")
        
    def test_download_logo(self):
        res = self.client.get(self.get_logo)
        self.assertEquals(res.status_code, 302)

    def test_get_single_coin(self):
        res = self.client.get(self.get_single_coin)
        self.assertEquals(res.status_code, 200)
        self.assertTemplateUsed(res,"coindata.html")
