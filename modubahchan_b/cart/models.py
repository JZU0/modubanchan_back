from django.db import models
from menu.models import Product
# Create your models here.

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    productList = models.ForeignKey(Product, on_delete=models.CASCADE)
    productNum = models.PositiveIntegerField()