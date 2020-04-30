from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulo

# Create your views here.

def busquedaProducto(request):

    return render(request, 'busqueda_productos.html')


def buscar(request):

    if request.GET['prd']:

        #mensaje='Articulo buscado: %r' %request.GET['prd']
        producto=request.GET['prd']

        articulos=Articulo.objects.filter(nombre__icontains=producto)

        return render(request,'resultados_busqueda.html', {'articulos':articulos, 'query':producto})

    else:
        return HttpResponse("No introduciste un carajo, pal lobby pete")
