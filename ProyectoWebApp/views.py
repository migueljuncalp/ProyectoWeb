from django.shortcuts import render,HttpResponse
import datetime  


# Create your views here.

def Home(request):
    now = datetime.date.today
    return render(request,'ProyectoWebApp/home.html',{'hora':now})



def Clientes(request):
    #guardamos todos los servicios
    return render(request,'ProyectoWebApp/clientes.html',{'servicios':"holas"})

def Contabilidad(request):
    return render(request,'ProyectoWebApp/contabilidad.html')
def Factura(request):
    return render(request,'ProyectoWebApp/factura.html')


