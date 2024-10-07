from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .form import RegisterForm
def register(response):
        if response.method == "POST":
            form = RegisterForm(response.POST)
            # print('hello')
            if form.is_valid():
                form.save()
                print('redirected')
                return redirect(reverse("Homepage"))
                
            # return redirect("main:home")
        else:
            form = RegisterForm()
            
        return render(response, "register/register.html",{"form": form})
# Create your views here.
