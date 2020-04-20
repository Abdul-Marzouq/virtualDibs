from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default = "")
    fullname = models.CharField(max_length=50,null='True',blank='True')
    DOB = models.DateField(null='True',blank='True')
    coins = models.FloatField(null='True',blank='True',default=0.0)
    def __str__(self):
        return self.user.username
