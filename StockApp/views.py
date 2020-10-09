from django.http import HttpResponse
from StockApp.models import Stock
from StockApp.forms import Stock ,StockCreateForm,StockSearchForm
from django.shortcuts import render, redirect

# Create your views here.
def home_stock(request):    
	title = 'Welcome: This is the Home Page'
	return render(request, "StockApp/Stock.html",{"title": title})

def list_stock(request):
    stock = Stock.objects.all()
    form = StockSearchForm(request.POST or None)
    title = 'Lista de productos'
    context = {
        "title":title,
        "stock":stock,
        "form":form
    }
    if request.method == 'POST':
	    stock = Stock.objects.filter(categoria__categoria__icontains=form['categoria'].value(),					
									)
	    context = {
	    "form": form,
	    "title": title,
	    "stock": stock,
        }
    return render(request, "StockApp/Stock.html",context)


def add_items(request):
    if request.method =='POST':
        form = StockCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listStock')
    else:
        form = StockCreateForm()
    context = {
		"form": form,
		"title": "Add Item",
	}
    return render(request, "StockApp/addToStock.html",context)


def producto_delete(request,id_producto):
    stock= Stock.objects.get(id=id_producto)
    if request.method == 'POST':
        stock.delete()
        return redirect('Stock')
    return render(request,'ProductosApp/productoDelete.html',{'Stock':stock})

