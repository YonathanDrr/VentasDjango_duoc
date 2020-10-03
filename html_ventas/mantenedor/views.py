from django.shortcuts import render
#from .forms import RegModelForm , ContactForm
#from .models import Registrado
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,"mantenedor/index.html")



def producto(request):
    return render(request,"mantenedor/Productos/FrProducto.html")



def modelo(request):
    return render(request,"mantenedor/Productos/FrModelo.html")


    
def marca(request):
    return render(request,"mantenedor/Productos/FrMarca.html")


    
def public(request):
    return render(request,"mantenedor/Publico/indexPublic.html")    


def login(request):
    return render(request,"mantenedor/Publico/loginPublic.html")        


def registrar(request):
    return render(request,"mantenedor/Publico/registrarPublic.html")    

""" def login(request):
    return render(request,"mantenedor/Productos/login.html") """
