from django.contrib import admin
from django.urls import  path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductoListado,ProductoCrear,ProductoDetalle,ProductoActualizar,ProductoEliminar


urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('', views.index, name = 'index'),
    path('FrProducto.html', views.producto, name = 'producto'),
    path('FrModelo.html', views.modelo, name = 'modelo'),
    path('FrMarca.html', views.marca, name = 'marca'),
    #path('loginPublic.html', views.login, name = 'logina'),
    #path('registrarPublic.html', views.registrar, name = 'registrar'),
    path('FrLogin.html', views.loginFr, name = 'loginFr'),
    path('listadoCurso.html', views.listadoCurso, name = 'listadoCurso'),
    path('agregarCursos.html', views.agregarCurso, name = 'agregarCurso'),
    path('modificarCursos.html/<id>/', views.modificarCurso, name = 'modificarCurso'),
    path('menu.html', views.menuMantenedor, name = 'menuMantenedor'),
    path('eliminarCursos.html/<id>/', views.eliminarCurso, name = 'eliminarCurso'),
    path('registro/',views.registrarUsuario,name='registrarUsuario'),

    #PATH PARA PUBLICO
    #----------------------------------------------------------------------------------------------------------------------------------------------#
    path('indexPublic.html', views.public, name = 'public'),
    path('compras.html', views.compra, name = 'compra'),
    path('perfil.html', views.perfil, name = 'perfil'),


    #----------------------------------------------------------------------------------------------------------------------------------------------#
    path('menuMantenedor/', ProductoListado.as_view(template_name = "mantenedor/Productos/indexb.html"), name='leer'),
    path('menuMantenedor/crear', ProductoCrear.as_view(template_name = "mantenedor/Productos/crear.html"), name='crear'),
    path('menuMantenedor/detalle/<int:pk>', ProductoDetalle.as_view(template_name = "mantenedor/Productos/detalles.html"), name='detalles'),
    path('menuMantenedor/editar/<int:pk>', ProductoActualizar.as_view(template_name = "mantenedor/Productos/actualizar.html"), name='actualizar'),
    path('menuMantenedor/eliminar/<int:pk>', ProductoEliminar.as_view(), name='eliminar'),

]


