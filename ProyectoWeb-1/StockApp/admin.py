from django.contrib import admin
from .models import Stock

# Register your models here.


from .forms import StockCreateForm

class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['categoria', 'nombre_producto', 'cantidad']
   form = StockCreateForm
   list_filter = ['categoria']
   search_fields = ['categoria', 'nombre_producto']

admin.site.register(Stock, StockCreateAdmin)