from django.shortcuts import render
from django.http import HttpResponse

def register(response):
    return render(response, "register/register.html",{})
# Create your views here.
