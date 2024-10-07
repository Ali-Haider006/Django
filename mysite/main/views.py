from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from .form import CreateNewList

# Create your views here.
def index(response,id):
    req = ToDoList.objects.get(id=id)
    # if response.method == "POST":
    #    if response.POST.get("save"):
    #        for item in req.item_set.all():
    #            if response.POST.get(str(item.id)) == "clicked":
    #                item.complete = False
    #            else: 
    #                 item.complete = True

    if response.POST.get("newItem"):
            txt = response.POST.get("new")
            complete = response.POST.get("itemComplete")
            if len(txt) > 2:
                req.item_set.create(text=txt,complete=complete)

            else:
                print('invalid')

    return render(response, 'main/list.html',{"name": req})

def name(response,name):
    req = ToDoList.objects.get(name = name)
    item = req.item_set.get()
    return render(response, 'main/list.html', {"name": req, "listData":item})
    # return HttpResponse('<h1>Name of List</h1>')


def homepage(response):
    return render(response,"main/home.html")

# def create(response,form):
#     form = CreateNewList()
#     return render(response, 'main/create.html', {"form":form})

def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():  # Validate the form
            name = form.cleaned_data['name']
            t = ToDoList(name= name)
            t.save()
            request.user.ToDoList.add(t)
            # Redirect or render a success page
            return HttpResponseRedirect("/%i"% t.id)
    else:
        form = CreateNewList()
    
    return render(request, 'main/create.html', {"form": form})

def view(response):
    return render(response, 'main/view.html',{})