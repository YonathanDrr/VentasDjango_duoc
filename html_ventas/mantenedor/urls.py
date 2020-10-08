from django.contrib import admin
from django.urls import  path 
from . import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('', views.index, name = 'index'),
    path('indexPublic.html', views.public, name = 'public'),
    path('FrProducto.html', views.producto, name = 'producto'),
    path('FrModelo.html', views.modelo, name = 'modelo'),
    path('FrMarca.html', views.marca, name = 'marca'),
    path('loginPublic.html', views.login, name = 'logina'),
    path('registrarPublic.html', views.registrar, name = 'registrar'),
    path('FrLogin.html', views.loginFr, name = 'loginFr'),
    path('listadoCurso.html', views.listadoCurso, name = 'listadoCurso'),
    path('agregarCursos.html', views.agregarCurso, name = 'agregarCurso'),
    path('modificarCursos.html/<id>/', views.modificarCurso, name = 'modificarCurso'),
    path('eliminarCursos.html/<id>/', views.eliminarCurso, name = 'eliminarCurso'),


]

