from django.shortcuts import render
from django.http import HttpResponse
from App.models import Usuarios, Compras, Productos
from App.forms import UsuariosFormularios, ComprasFormularios, ProductosFormularios
# Create your views here.
def inicio(request):
    return render(request, 'inicio2.html')
def contactanos(request):
    return render(request, 'contactanos.html')
def productos(request):
    return render(request, 'productos.html')
def locales(request):
    return render(request, 'locales.html')
def UsuariosFormulario(request):
    if request.method == 'POST':
        usuarios = UsuariosFormularios(request.POST)
        print(usuarios)
        if usuarios.is_valid:
            informacion = usuarios.cleaned_data
            usuarios2 = Usuarios(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            usuarios2.save()
            return render(request, "inicio2.html")
    else:
        usuarios = UsuariosFormularios()

    return render(request, "usuariosformulario.html", {"usuarios_formulario": usuarios})

def BusquedaUsuarios(request):
    return render(request, 'BusquedaUsuarios.html')

def Buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        usuario = Usuarios.objects.filter(nombre__icontains=nombre)
        return render(request, 'resultadoBusquedaUsuarios.html', {'nombre':nombre, 'usuario':usuario})
    else:
        respuesta = "no enviaste datos"
    return HttpResponse(respuesta)

def ComprasFormulario(request):
    if request.method == 'POST':
        compras = ComprasFormularios(request.POST)
        print(compras)
        if compras.is_valid:
            informacion = compras.cleaned_data
            compras2 = Compras(articulo=informacion['articulo'], cantidad=informacion['cantidad'], comprador=informacion['comprador'])
            compras2.save()
            return render(request, "inicio2.html")
    else:
        compras = ComprasFormularios()
    return render(request, "comprasformulario.html", {"compras_formulario": compras})

def BusquedaCompras(request):
    return render(request, "BusquedaCompras.html")

def BuscarC(request):
    if request.GET['articulo']:
        articulo = request.GET['articulo']
        compra = Compras.objects.filter(articulo__icontains=articulo)
        return render(request, 'resultadoBusquedaCompras.html', {'articulo':articulo, 'compra':compra})
    else:
        respuesta = "no enviaste datos"
    return HttpResponse(respuesta)

def ProductosFormulario(request):
    if request.method == 'POST':
        productos = ProductosFormularios(request.POST)
        print(productos)
        if productos.is_valid:
            informacion = productos.cleaned_data
            productos2 = Productos(producto=informacion['producto'], cantidad_disponible=informacion['cantidad_disponible'], precio=informacion['precio'])
            productos2.save()
            return render(request, "inicio2.html")
    else:
        productos = ProductosFormularios()
    return render(request, "productosformulario.html", {'productos_formulario':productos})

def BusquedaProductos(request):
    return render(request, "BusquedaProductos.html")

def BuscarP(request):
    if request.GET['producto']:
        producto = request.GET['producto']
        producto2 = Productos.objects.filter(producto__icontains=producto)
        return render(request, 'resultadoBusquedaProducto.html', {'producto':producto, 'producto2':producto2})
    else:
        respuesta = 'no enviaste datos'
    return HttpResponse(respuesta)