from django.db import models
from accounts.models import User
from menu.models import *
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, null=True, blank=True)
    memo = models.TextField(null=True, blank=True)