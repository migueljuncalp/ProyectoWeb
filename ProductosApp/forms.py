from django import forms

from ProductosApp.models import categoriaProducto , Producto


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = categoriaProducto

        fields = [
            'categoria',
        ]
        labels = {
            'categoria':'Nombre de la Categoria',
        }
        widgets = {
            'categoria': forms.TextInput(attrs={'class':'form-control'})
        }


class ProductoForm(forms.ModelForm):

    class Meta:
        model =Producto

        fields = [
            'nombre_producto',
            'precio_sin_iva',
            'precio_iva',
            'categoriaProducto',
        ]
        labels = {
            'nombre_producto':'Nombre del producto',
            'precio_sin_iva':'Precio sin IVA',
            'precio_iva':'Precio con IVA',
            'categoriaProducto':'Selecciona categoría del producto',
        }
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class':'form-control'}),
            'precio_sin_iva': forms.NumberInput(attrs={'class':'form-control'}),
            'precio_iva': forms.NumberInput(attrs={'class':'form-control'}),
            'categoriaProducto':forms.Select(attrs={'class':'form-control'}),
        }