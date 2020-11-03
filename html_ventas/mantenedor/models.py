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

        def __str__(self) : #Python 3   como se debe renderizar el objeto puede ser por nombre,email o lo que uno desee que se muestre
            return self.email

 

class Persona(models.Model):
    nombrePersona = models.CharField(max_length=50,verbose_name="Nombre Persona")
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
        return self.nombrePersona + ' ' + self.apellidoPersona


class Descuento(models.Model) :
    porcentaje = models.FloatField(max_length=4)
    
    class Meta:
        db_table ='descuento'



class Comuna(models.Model) :
    idcomuna = models.CharField( max_length=100)
    nombre = models.CharField( max_length=100)
    
    class Meta:
        db_table ='comuna'

    def __str__(self):
        return self.nombre
    
class Region(models.Model) :
    idcom = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name="IdComuna")
    nombre = models.CharField( max_length=100)
    class Meta:
        db_table ='region'

    
    def __str__(self) : #Python3
        return self.nombre

class Curso(models.Model):
    titulo = models.CharField( max_length=50)
    descripcion = models.TextField( max_length=70)
    anio = models.CharField( max_length=50)
    precio = models.IntegerField() 
    autor = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    comunaFk = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name="ComunaId")
    direccion = models.CharField( max_length=50)
    imagen = models.ImageField(upload_to="curso", null=True)
    
    class Meta:
        db_table = 'curso'

class DetalleCurso(models.Model) :
    codDesc =models.ForeignKey(Descuento, on_delete=models.CASCADE) 
    codCurso =models.ForeignKey(Curso, on_delete=models.CASCADE)
    duracion = models.IntegerField()
    cantidadClass = models.IntegerField()
    temporada = models.CharField(max_length=10)
    nivel = models.CharField(max_length=15)
    idioma = models.CharField(max_length=15)
    class Meta:
        db_table ='detalleCurso'


class Producto(models.Model):
    nombre = models.CharField( max_length=50)
    marca = models.CharField( max_length=50)
    modelo = models.CharField( max_length=50)
    precio = models.IntegerField(null=True) 
    talla = models.CharField( max_length=3)

    class Meta:
        db_table = 'producto'

class DetalleProducto(models.Model) :
    codProd =models.ForeignKey(Producto, on_delete=models.CASCADE)
    codDesc =models.ForeignKey(Descuento, on_delete=models.CASCADE)
    duracion = models.IntegerField(null=True)
    stock = models.IntegerField(null=True)
    color = models.CharField(max_length=10,null=True)
    nivel = models.CharField(max_length=15,null=True)
    idioma = models.CharField(max_length=15,null=True)
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
    












