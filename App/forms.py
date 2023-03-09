from django import forms

class UsuariosFormularios(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class ComprasFormularios(forms.Form):
    articulo = forms.CharField()
    cantidad = forms.IntegerField()
    comprador = forms.CharField()

class ProductosFormularios(forms.Form):
    producto = forms.CharField()
    cantidad_disponible = forms.IntegerField()
    precio = forms.IntegerField()