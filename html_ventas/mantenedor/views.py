from django.shortcuts import render, redirect
#from .forms import RegModelForm , ContactForm
#from .models import Registrado
from django.http import HttpResponse
from.models import Producto
from .forms import ProductoForm




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



def loginFr(request):
    return render(request,"mantenedor/General/FrLogin.html")        





def agregarCurso(request):
    data = {
        'form':ProductoForm
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Curso agregado exitosamente"
#nuevo formulario
    #data['form'] = formulario

    return render(request,"mantenedor/Publico/agregarCursos.html",data)


def listadoCurso(request):
    listadoCursos = Producto.objects.all()
    data = {
        'listadoCursos': listadoCursos
    }
    return render(request,"mantenedor/Publico/listadoCurso.html",data)


def modificarCurso(request, id) :
    producto = Producto.objects.get( id = id ) 
    data = {
        'form': ProductoForm(instance = producto)
    }

    if request.method == 'POST' :
        formulario = ProductoForm(data = request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificación Exitosa !!"
            data['form'] = formulario
#nuevo formulario
    #data['form'] = formulario

    return render(request,"mantenedor/Publico/modificarCursos.html", data)


def eliminarCurso(request, id) :
    producto = Producto.objects.get(id = id)
    producto.delete()
    data = {
        'form': ProductoForm
    }

    if producto.is_valid():
        data['mensaje'] = "Eliminado !!"

           
    return redirect(to='listadoCurso')
    