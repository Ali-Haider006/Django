from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.
def index(response,id):
    req = ToDoList.objects.get(id = id)
    item = req.item_set.get()
    return HttpResponse("<h1>%s%s</h1> " %(req,item.text))

def name(response,name):
    req = ToDoList.objects.get(name = name)
    item = req.item_set.get()
    return HttpResponse("<h1>%s</h1>" %(item.text))


def homepage(response):
    return HttpResponse("<h1> First Page</h1>")