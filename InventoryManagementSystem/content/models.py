from django.db import models

# Create your models here.
class Asset(models.Model):
    name = models.CharField(max_length=64)
    count = models.IntegerField() #quantity in stock
    cost=models.FloatField() #cost price
    price=models.FloatField() #sale price