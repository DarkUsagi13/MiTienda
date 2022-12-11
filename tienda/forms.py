from django import forms

from tienda import models
from tienda.models import Producto, Marca


class FormularioMarca(forms.ModelForm):
    class Meta:
        model = Marca
        fields = "__all__"


class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"


class FormularioBusqueda(forms.Form):
    nombre = forms.CharField(max_length=20)