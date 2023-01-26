from django.contrib import admin
from django.urls import path
from . import views
#from pildorasinformaticas.views import module

app_name = "pildoras"

urlpatterns = [
    path('', views.HelloWorld),
    path('fecha/',views.getDate),
    path('edad/<int:age>/<int:year>',views.calculAge),
]