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
    path('loginPublic.html', views.login, name = 'login'),
    path('registrarPublic.html', views.registrar, name = 'registrar'),

    
    

   

]


"""  path('login.html', views.login, name = 'index')"""