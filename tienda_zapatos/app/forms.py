from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields = ["usuario", "nombre", "apellido", "correo", "edad"]
        fields = '__all__'