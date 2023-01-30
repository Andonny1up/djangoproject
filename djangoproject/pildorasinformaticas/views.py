from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import loader

class Person():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        

# Create your views here.
def HelloWorld(request):
    juan = Person("Juan","Perez")
    return render(request,"pildorasinformaticas/template.html",{
        "persona": juan,
        "themes": ["templates","Models","Forms","views","Deploy"]
    })
    
    #otra forma de carga::
    # juan = Person("Juan","Perez")
    # extern_doct = loader.get_template('pildorasinformaticas/template.html')
    # contex = {
    #     "persona": juan,
    #     "themes": ["templates","Models","Forms","views","Deploy"]
    # }
    # documento =  extern_doct.render(contex)
    # return HttpResponse(documento)


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


def hijo_uno(request):
    current_date = datetime.datetime.now()
    
    return render(request,"pildorasinformaticas/hijo1.html",{
        "date":current_date
    })
    

def hijo_dos(request):
    current_date = datetime.datetime.now()
    
    return render(request,"pildorasinformaticas/hijo2.html",{
        "date":current_date
    })