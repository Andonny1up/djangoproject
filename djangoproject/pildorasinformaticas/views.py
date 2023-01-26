from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def HelloWorld(request):
    return HttpResponse("Hello world")


def getDate(request):
    current_date = datetime.datetime.now()
    document = """
    <h1>
        Fecha y hora Actual: %s
    </h1>
    """ % current_date
    return HttpResponse(document)

def calculAge(request,age,year):
    #age = 18
    perid = year - 2019
    future_age = age + perid
    document ="""
    <h2>En el año %s tendrás %s años </h2>
    """%(year,future_age)
    return HttpResponse(document)