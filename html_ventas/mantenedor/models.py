from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registrado(models.Model):
    nombre = models.CharField( max_length=100, blank=True, null=True )
    email = models.EmailField()
    timestamp = models.DateTimeField( auto_now_add=True, auto_now=False)
    class Meta:
        db_table ='registrado'

    def __unicode__(self) : #Python 2
        return self.email

        def __str__(self) : #Python 3
            return self.email



class Persona(models.Model):
    nombrePersona = models.CharField(max_length=50)
    apellidoPersona = models.CharField(max_length=50)
    sexo = models.CharField(max_length=15, null = True)
    email = models.EmailField()
    rut = models.CharField(max_length=13, null = True)
    celular = models.CharField(max_length = 15 , null = True)
      
    class Meta:
        db_table ='persona'

    def __unicode__(self) : #Python 2
        return self.email

        def __str__(self) : #Python 3
            return self.email


class Descuento(models.Model) :
    porcentaje = models.FloatField(max_length=4)
    
    class Meta:
        db_table ='descuento'



class Comuna(models.Model) :
    idcomuna = models.CharField( max_length=100)
    nombre = models.CharField( max_length=100)
    
    class Meta:
        db_table ='comuna'


    
class Region(models.Model) :
    idcom = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    nombre = models.CharField( max_length=100)
    
    class Meta:
        db_table ='region'



class Producto(models.Model) :
    nombre = models.CharField( max_length=50)
    marca = models.CharField( max_length=50)
    modelo = models.CharField( max_length=50)
    precio = models.IntegerField()
    talla = models.CharField(max_length=3)
    
    class Meta:
        db_table ='producto'



class DetalleProducto(models.Model) :
    codProd =models.ForeignKey(Producto, on_delete=models.CASCADE)
    codDesc =models.ForeignKey(Descuento, on_delete=models.CASCADE)
    stock = models.IntegerField()
    color = models.CharField( max_length=10)
    tipo = models.CharField(max_length=10)
    material = models.CharField(max_length=3)
    
    class Meta:
        db_table ='detallePro'


class Contacto(models.Model) :
    nombre = models.CharField( max_length=50)
    email = models.EmailField()
    descripcion = models.CharField( max_length=50)
    
    class Meta:
        db_table ='contacto'


    def __unicode__(self) : #Python2
        return self.email

        def __str__(self) : #Python3
            return self.email
    
        
class boleta (models.Model) :
    codDetalle =models.ForeignKey(DetalleProducto, on_delete=models.CASCADE)
    codPersona =models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha= models.DateTimeField( auto_now_add=True, auto_now=False)
    nombre = models.CharField( max_length=10)
    email = models.EmailField()
    
    class Meta:
        db_table ='boleta'

    def __unicode__(self) : #Python2
        return self.email
    
        def __str__(self) : #Python3
            return self.email
    












