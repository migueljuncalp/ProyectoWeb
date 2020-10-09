
from django import forms
from .models import Stock


class StockCreateForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['categoria', 'nombre_producto', 'cantidad','precio_de_compra']

class StockSearchForm(forms.ModelForm):
   categoria=forms.ChoiceField(required=False)
   class Meta:
     model = Stock
     fields = ['categoria']