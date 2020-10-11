from django import forms
from django.forms import ModelForm
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Se realiza el tipo de form que se quiere mostrar
class ProductoForm(ModelForm):

    #Validaciones
    nombre = forms.CharField(min_length=2, max_length=15, required=True)
    precio = forms.IntegerField(min_value=1, max_value=700) 
    
    class Meta:
        model = Producto
        fields = ['nombre', 'marca','modelo','precio','talla']

        #widget para modificar la fecha
        """ widgets = {
            'nombre_atributo' : forms.SelectDateWidget(years = range(1920,2020))

        } """

    #validacion de fecha para que no sea superior a la fecha de el dia que se esta subiendo.
    #despues de crear la validacion dirigirse al views, sobreescribir el data con el nuevo formulario


    def clean_fecha_subida(self):
        fecha = self.clean_data('fecha_subida')

        if fecha > datetime.date.today():
            raise forms.ValidationError("La fecha no se puede ser mayo al del dia de hoy")

        return fecha

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['first_name','last_name','email','username','password1','password2']

   
    