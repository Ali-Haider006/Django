from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .form import CreateNewList
# Create your views here.
def index(response,id):
    req = ToDoList.objects.get(id = id)
    # item = req.item_set.get()
    return render(response, 'main/list.html',{"name": req})

def name(response,name):
    req = ToDoList.objects.get(name = name)
    item = req.item_set.get()
    return render(response, 'main/home.html', {"name": req, "listData":item})


def homepage(response):
    return HttpResponse("<h1> First Page</h1>")

def create(response):
    form = CreateNewList()
    return render(response, 'main/create.html', {"form":form})