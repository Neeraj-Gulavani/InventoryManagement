from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Asset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64) #product name
    count = models.IntegerField() #quantity in stock
    cost=models.FloatField() #cost price
    price=models.FloatField() #sale price