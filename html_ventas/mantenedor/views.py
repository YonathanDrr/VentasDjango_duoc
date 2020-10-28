from django.shortcuts import render, redirect
#from .forms import RegModelForm , ContactForm
#from .models import Registrado
from django.http import HttpResponse
from.models import Producto,Persona
from .forms import ProductoForm, CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login,authenticate
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

 
from django.urls import reverse
 
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
 
from django import forms



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

def menuMantenedor(request):
    return render(request,"mantenedor/Publico/menu.html")          

def menuBase(request):
    return render(request,"mantenedor/Publico/menuBase.html")         

def perfil(request):
    return render(request,"mantenedor/Publico/perfil.html")          

def compra(request):
    return render(request,"mantenedor/Publico/compras.html")          


def personaListado(request):
    persona = Persona.objects.all()
    print("registro",persona)
    return render(request,"mantenedor/Persona/indexPersona.html",{'PersonaRegistros' : persona})      


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

    return render(request,"mantenedor/Productos/agregarCursos.html",data)


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


class ProductoListado(ListView): 
    model = Producto
 
class ProductoDetalle(DetailView): 
    model = Producto
 
class ProductoCrear(SuccessMessageMixin, CreateView): 
    model = Producto
    form = Producto
    fields = "__all__" 
    success_message = 'Producto Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre     
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 
 
class ProductoActualizar(SuccessMessageMixin, UpdateView): 
    model = Producto
    form = Producto
    fields = "__all__"  
    success_message = 'Producto Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 
 
class ProductoEliminar(SuccessMessageMixin, DeleteView): 
    model = Producto 
    form = Producto
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'


    
""" def myfirstview(request):
    data = {
        'name': 'Yonathan',
        'cursos' : Curso.objects.all()
    }
    return render(request, "mantenedor/newTemplates/indexNew.html",data) """