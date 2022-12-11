from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from tienda.forms import FormularioMarca, FormularioProducto, FormularioBusqueda
from tienda.models import Producto


# Create your views here.


def welcome(request):
    return render(request, 'tienda/welcome.html', {})


def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/gestion/listado.html', {'productos': productos})


def crear_marca(request):
    marca = {}
    form = FormularioMarca(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, "Marca creada correctamente")
        return redirect('listado productos')
    marca['form'] = form
    return render(request, 'tienda/gestion/crear_marca.html', marca)


def crear_producto(request):
    producto = {}
    form = FormularioProducto(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, "Producto creado correctamente")
        return redirect('listado productos')
    producto['form'] = form
    return render(request, 'tienda/gestion/crear_producto.html', producto)


def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    form = FormularioProducto(instance=producto)
    if request.method == 'POST':
        form = FormularioProducto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Registro editado')
            return redirect('listado productos')
    form = {'form': form}
    return render(request, 'tienda/gestion/editar_producto.html', form)


def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.add_message(request, messages.INFO, 'Producto ' + producto.nombre + ' eliminado correctamente')
        return redirect('listado productos')
    return render(request, 'tienda/gestion/eliminar_producto.html', {'producto': producto})


def buscar(request):
    form = FormularioBusqueda(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            filtro = Producto.objects.filter(nombre__contains=nombre).values()
            return render(request, "tienda/gestion/buscar.html", {'form': form, 'filtro': filtro})
    return render(request, "tienda/gestion/buscar.html", {'form': form})
