from cgi import print_directory
from django.db import models
from accounts.models import User
# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    price = models.PositiveIntegerField()
    description = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    feedText = models.TextField()
    CARTEGORY_LIST = (
        ('DS', 'Dessert'),
        ('BV', 'Beverage'),
        ('AC', 'Alcohol'),
        ('SD', 'SideDish'),
        ('MK', 'MealKit'),
        ('AP', 'ALP'),
    )
    ## 프론트에서 가져올때 : menu.category 는 키값, menu.get_category_display 는 내용
    category = models.CharField(max_length=2, choices=CARTEGORY_LIST)
    picture = models.ImageField(upload_to = "menu/", blank=True, null=True)

    # def __str__(self):
    #     return self.name
