from django.db import models


class CoinDataModel(models.Model):
    name = models.CharField(max_length=14 ,unique=True)
    price = models.CharField(max_length=50)
    symbol = models.CharField(max_length=12,unique=True)

    def __str__(self):
        return self.name
    