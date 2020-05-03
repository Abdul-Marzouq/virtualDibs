from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from model_utils import Choices
from django.utils.translation import gettext as _

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default = "")
    fullname = models.CharField(max_length=50,null='True',blank='True')
    DOB = models.DateField(null='True',blank='True')
    coins = models.FloatField(null='True',blank='True',default=0.0)

    def __str__(self):
        return self.user.username

class Address(models.Model):
    TYPE_OF_ADDRESS = Choices(
       (1, 'delivery_address', _('Address to which items will be delivered.')),
       (2, 'dispatch_address', _('Address from where items will be dispatched.')),
    )
    customer = models.ForeignKey(Customer,default=1,on_delete=models.SET_DEFAULT)
    type = models.PositiveSmallIntegerField(
       choices=TYPE_OF_ADDRESS,
       default=TYPE_OF_ADDRESS.delivery_address,
   )
    address = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zipcode = models.CharField(max_length=6, default="331651")
    country = models.CharField(max_length=50)
