from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Merch


def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", {'bands': bands})


def about(request):
    return render(request,"listings/about.html")


def listings(request):
    merchs = Merch.objects.all()
    return render(request,"listings/listing.html", {'merches':merchs})


def contact(request):
    return render(request,"listings/contact.html")
