from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):

    return render(request,"home.html")

def login_page(request):
    return render(request,"login.html")

def about_page(request):
    return render(request,"about.html")

def track_page(request):
    return render(request,"track.html")
