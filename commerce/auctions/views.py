from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms

from .models import *

class Add_product_Form(forms.Form):
    product_name = forms.CharField(max_length=64)
    product_description = forms.CharField(widget=forms.Textarea)
    category = forms.CharField(max_length=64)
    link = forms.URLField()
    price = forms.IntegerField()

def index(request):
    items = Product.objects.all()
    #try:
     #   watch_list_count  = Watch_list.objects.filter(user=)

    return render(request, "auctions/index.html",{
        "items":items
    })



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


    
    
@login_required
def my_products(request, username):
    id = User.objects.get(username=username).pk
    user = User.objects.get(pk=id)
    list_of_product = user.products.all()
    
    return render(request, "auctions/my_product.html", {
        "list_of_product":list_of_product
    })

@login_required
def add_watchlist(request, product_ID):
    pass

@login_required
def watchlist(request):
    return render(request, "auctions/watchlist.html")

@login_required
def create_listing(request):
    return render(request, "auctions/create_listing.html", {
        "form": Add_product_Form()
    })


@login_required
def your_winnings(request):
    return render(request, "auctions/your_winnings.html")
