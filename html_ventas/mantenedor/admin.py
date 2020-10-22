from django.contrib import admin

from .models import Producto,Registrado,Persona,Descuento,Comuna,Region,Producto,DetalleProducto,Contacto,boleta

class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombrePersona','apellidoPersona','rut','email','celular']
    search_fields = ['rut','email']
    list_filter = ['sexo']
    list_per_page=10

admin.site.register(Producto)
#admin.site.register(Registrado)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Descuento)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(DetalleProducto)
admin.site.register(Contacto)
admin.site.register(boleta) 

