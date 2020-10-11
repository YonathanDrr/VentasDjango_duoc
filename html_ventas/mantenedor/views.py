from django.shortcuts import render, redirect
#from .forms import RegModelForm , ContactForm
#from .models import Registrado
from django.http import HttpResponse
from.models import Producto
from .forms import ProductoForm, CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login,authenticate




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


""" def registrar(request):
    return render(request,"mantenedor/Publico/registrarPublic.html")    
 """


def loginFr(request):
    return render(request,"mantenedor/General/FrLogin.html")        




@login_required
def agregarCurso(request):
    data = {
        'form':ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
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
        formulario = ProductoForm(data = request.POST, instance = producto,files=request.FILES)
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
   
           
    return redirect(to='listadoCurso')
    

def registrarUsuario(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()

            data['mensaje'] ="Usuario Registrado Correctamente"
            return redirect(to='login')
            

            #autenticar al usuario y rederigirlo al inicio
            """ username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect(to='public')
 """
    return render(request,'registration/registrar.html',data)