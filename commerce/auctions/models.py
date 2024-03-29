from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    pass


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    owner_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    item_name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    description = models.TextField(max_length=64, blank=True)
    link = models.CharField(max_length=64, default=None, blank=True, null=True)
    time = models.DateTimeField(default=timezone.now)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.item_name}"

class All_Won(models.Model):
    id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=64)
    item_name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    description = models.TextField(max_length=64, blank=True)
    link = models.CharField(max_length=64, default=None, blank=True, null=True)
    time = models.CharField(max_length=64)
    

class Watch_list(models.Model):
    u_ID = models.IntegerField()
    p_ID = models.IntegerField()


class Comment_Table(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name="person_in_comments")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_in_comments")
    comment = models.TextField()
    time = models.DateTimeField(default=timezone.now)

class Bid(models.Model):
    Bid = models.IntegerField()
    bid_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="all_bids")
    on_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="Bid")

class Winner(models.Model):
    won_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="winings")
    product_won = models.ForeignKey(All_Won, on_delete=models.CASCADE, related_name="item_won")
    on_price = models.IntegerField()


    