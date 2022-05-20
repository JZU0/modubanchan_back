import imp
from django.db import models
from menu.models import Product
from accounts.models import User
# Create your models here.

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    productList = models.ForeignKey(Product, on_delete=models.CASCADE)
    productNum = models.PositiveIntegerField()