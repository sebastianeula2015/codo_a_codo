from django import forms
from django.core.exceptions import ValidationError
from .models import Cliente

provincias = [
    [0, "Mendoza"],
    [1, "San Luis"],
    [2, "San Juan"],
    [3, "La Rioja"],
    [4, "Neuquen"],
]


class NuevoClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class': "form-control ", 'placeholder': 'Ingrese su nombre'}))
    apellido = forms.CharField(label="Apellido", required=True,                           widget=forms.TextInput(attrs={'class': "form-control ", 'placeholder': 'Ingrese su apellido'}))
    dni = forms.IntegerField(label="DNI", required=True, widget=forms.TextInput(attrs={'class': "form-control ", 'placeholder': 'Ingrese su numero de documento'}))
    email = forms.EmailField(label="Correo Electronico", required=True, widget=forms.TextInput(attrs={'class': "form-control ", 'placeholder': 'Ingrese su correo electronico'}))
    telefono = forms.EmailField(label="Teléfono", required=True, widget=forms.TextInput(attrs={'class': "form-control ", 'placeholder': 'Ingrese su teléfono'}))
    provincia = forms.CharField(label="Provincia", required=True, widget=forms.TextInput(attrs={'class': "form-control ", 'placeholder': 'Provincia de pertenencia'}))
    direccion = forms.CharField(label="Direccion", required=True, widget=forms.TextInput(attrs={'class': "form-control separador", 'placeholder': 'Direccion de facturación'}))
        #









# ESTA ES OTRA FORMA DE HACERLO MAS MANUAL POR ASI DECIRLO

# class ClienteNuevoForm(forms.Form):
#     nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
#         attrs={'class': "form-control ", 'placeholder': 'ingrese su nombre'}))
#     apellido = forms.CharField(label="Apellido", required=True,
#                            widget=forms.TextInput(attrs={'class': 'form-group label-label'}))
#     dni = forms.IntegerField(label="DNI", required=True, widget=forms.TextInput(attrs={'class': 'form-group label-label'}))
#     email = forms.EmailField(label="email", required=True,
#                          widget=forms.TextInput(attrs={'class': 'form-group label-label'}))
#     provincias = forms.ChoiceField(label="Provincias", choices=provincias)
#     direccion = forms.CharField(label="Direccion", required=True,
#                             widget=forms.TextInput(attrs={'class': 'form-group label-label'}))
#
#
#     def clean_nombre(self):
#         if not self.cleaned_data["nombre"].isalpha():
#             raise ValidationError("Error en el campo nombre")
#         return self.cleaned_data["nombre"]
#
#
# class ClienteModificacionForm(forms.Form):
#     nombre = forms.CharField(label="Nombre", required=True)
#     apellido = forms.CharField(label="Apellido", required=True)
#     dni = forms.IntegerField(label="DNI", required=True)
#     email = forms.EmailField(label="email", required=True)
#     direccion = forms.CharField(label="Direccion", required=True)
#
#     def clean_nombre(self):
#         if not self.cleaned_data["nombre"].isalpha():
#             raise ValidationError("Error en el campo nombre")
#
#         return self.cleaned_data["nombre"]
