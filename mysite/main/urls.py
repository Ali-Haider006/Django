#Paths to our webpages
from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>",views.index,name="index"),
    # path("<str:name>",views.name,name="name"),
    path("",views.homepage,name="Homepage"),
    path('create',views.create,name="create"),
    path('view/',views.view,name="view"),
]