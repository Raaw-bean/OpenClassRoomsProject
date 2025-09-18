from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Merch


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
                        <h1>Hello Django!</h1>
                        <p>My Favorite Bands are : </p>
                        <ul>
                            <li>{bands[0].name}</li>
                            <li>{bands[1].name}</li>
                            <li>{bands[2].name}</li>
                        </ul>
                        """)

def about(request):
    return HttpResponse('<h1>About-Us</h1>  <p>We love merch!</p>')

def listings(request):
    merchs = Merch.objects.all()
    return HttpResponse(f"""
                        <ul>
                            <li>{merchs[0].title}</li>
                            <li>{merchs[1].title}</li>
                            <li>{merchs[2].title}</li>
                        </ul>
                        """)

def contact(request):
    return HttpResponse('<h1>Contact Us</h1>  <p>Wait for the acquisition...XD</p>')