from django.shortcuts import render,redirect
from django.http import HttpResponse
from ProductosApp.models import categoriaProducto , Producto 
from ProductosApp.forms import CategoriaForm , ProductoForm
# Create your views here.


def mostrar_categorias(request):
    categorias= categoriaProducto.objects.all()
    return render(request,'ProductosApp/categoriaProducto.html',{'categorias':categorias})

def categoria_add(request):
    if request.method =='POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('categorias')
    else:
        form = CategoriaForm()
    
    return render(request ,'ProductosApp/categoriaForm.html',{'form':form})


def categoria_edit(request,id_categoria):
    categoria = categoriaProducto.objects.get(id=id_categoria)
    if request.method =='GET':
        form = CategoriaForm(instance=categoria)
    else:
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
        return redirect('categorias')

    return render(request,'ProductosApp/categoriaForm.html',{'form':form})

def categoria_delete(request,id_categoria):
    categoria= categoriaProducto.objects.get(id=id_categoria)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categorias')
    return render(request,'ProductosApp/categoriaDelete.html',{'categoria':categoria})



###-----------------------Productos-------------------------------------#####

def mostrar_productos(request):
    productos= Producto.objects.all()
    return render(request,'ProductosApp/productos.html',{'productos':productos})



def producto_add(request):
    if request.method =='POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('productos')
    else:
        form = ProductoForm()
    
    return render(request ,'ProductosApp/productoForm.html',{'form':form})

def producto_edit(request,id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method =='GET':
        form = ProductoForm(instance=producto)
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('productos')

    return render(request,'ProductosApp/productoForm.html',{'form':form})


def producto_delete(request,id_producto):
    producto= Producto.objects.get(id=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    return render(request,'ProductosApp/productoDelete.html',{'producto':producto})

