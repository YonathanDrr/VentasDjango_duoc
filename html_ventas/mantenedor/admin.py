from django.contrib import admin

from .models import Producto,Registrado,Persona,Descuento,Comuna,Region,Producto,DetalleProducto,Contacto,boleta

admin.site.register(Producto)
admin.site.register(Registrado)
admin.site.register(Persona)
admin.site.register(Descuento)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(DetalleProducto)
admin.site.register(Contacto)
admin.site.register(boleta) 

