from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    DOB = models.DateField()
    dispatch_address_id = models.IntegerField()
    delivery_address_id = models.IntegerField()
    coins = models.FloatField()

class Object(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    start_price = models.FloatField()
    sale_status = models.BooleanField()
    approval_status = models.BooleanField()
    seller_id = models.IntegerField()

class Event(models.Model):
    seller_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

class ApprovedEvents(models.Model):
    event_id = models.IntegerField()
    no_of_bids = models.IntegerField()
    final_bidding_price = models.FloatField()
    buyer_id = models.IntegerField()
    transaction_id = models.IntegerField()

class UnapprovedEvents(models.Model):
    event_id = models.IntegerField()
    penalty_amount = models.FloatField()
    penalty_reason = models.CharField(max_length=200)

class Currency(models.Model):
    name = models.CharField(max_length=30)
    coins_exchange_rate = models.FloatField()

class Bids(models.Model):
    bidder_id = models.IntegerField()
    event_id = models.IntegerField()
    bidding_amount = models.FloatField()
    bid_finalized_flag = models.BooleanField()

class Transactions(models.Model):
    dispatch_status = models.BooleanField()
    delivery_status = models.BooleanField()
    company_profits = models.FloatField()

class Address(models.Model):
    house_name = models.CharField(max_length=25)
    street = models.CharField(max_length=25)
    district = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=30)
    zip = models.IntegerField()
