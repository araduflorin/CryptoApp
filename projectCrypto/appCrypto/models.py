
from django.db import models

class Coin(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)
    price_usd = models.FloatField()
    icon_url = models.URLField()

    def __str__(self):
        return self.name

