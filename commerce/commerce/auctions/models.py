from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction_listing(models.Model):
    name_owner = models.CharField(max_length=64)
    title_name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    description = models.TextField(max_length=64)
    link = models.CharField(max_length=64, default=None, blank=True, null=True)
    time = models.CharField(max_length=64)
    price = models.IntegerField()

class Bids(models.Model):
    user_name = models.CharField(max_length=64)
    title_name = models.CharField(max_length=64)
    listing_ID = models.IntegerField()
    bid = models.IntegerField()
    

class Comments():
    user_name = models.CharField(max_length=64)
    time = models.CharField(max_length=64)
    comment = models.TextField()
    listing_ID = models.IntegerField()

class Watch_list(models.Model):
    user_name = models.CharField(max_length=64)
    listing_ID = models.IntegerField()

class Close_Bid(models.Model):
    owner_name = models.CharField(max_length=64)
    winner_name = models.CharField(max_length=64)
    listing_ID = models.IntegerField()
    win_price = models.IntegerField()


class All_Listing(models.Model):
    listing_ID = models.IntegerField()
    title_name = models.CharField(max_length=64)
    description = models.TextField()
    link = models.CharField(max_length=64, default=None, blank=True, null=True)

