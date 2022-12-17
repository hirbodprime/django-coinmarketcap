from django.db import models
from django.core.files import File  # you need this somewhere
import urllib
import os
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # random_num = random.randint(1, 27634721234561)
    name, ext = get_filename_ext(filename)
    # final_name = f"{random_num}-{instance.symbol}-{name}{ext}"
    return f"logo/{instance.symbol}/{instance.symbol}.jpg"

class CoinDataModel(models.Model):
    name = models.CharField(max_length=14 ,unique=True)
    price = models.CharField(max_length=50)
    symbol = models.CharField(max_length=12,unique=True)
    image = models.ImageField(upload_to=upload_image_path ,null=True,blank=True)
    def __str__(self):
        return self.symbol



