from django.shortcuts import render,redirect
from django.http import HttpResponse
from Productos.models import Categoria,Producto,Venta
from Productos.forms import addProductosForm,addCategoriasForm


def index(request):
 	return render(request,'base/index.html')

def productos(request):		
	productos_list = Producto.objects.all().order_by('Nombre')
	contexto = {'productos_list':productos_list}
	return render(request,'tienda/productos.html', contexto)	

def categorias(request):		
	categorias_list = Categoria.objects.all().order_by('id_Cat')
	contexto = {'categorias_list':categorias_list}
	return render(request,'tienda/categorias.html', contexto)	

def ventas(request):
 	ventas_list = Venta.objects.all() 	
 	contexto = {'ventas_list':ventas_list}

 	return render(request, 'tienda/ventas.html', contexto)

 	
 # ALTAS, BAJAS ,CAMBIOS --- PRODUCTOS

def productos_view(request):
 	if request.method == 'POST':
 		form = addProductosForm(request.POST)
 		if form.is_valid():
 			form.save()
 		return redirect('productos:listaProductos')
 	else:
 		form = addProductosForm()
 	return render(request, 'forms/nuevoProductoForm.html',{'form':form})

def producto_edit(request, id_Prod):
	objetoProd = Producto.objects.get(id_Prod = id_Prod)
	if request.method == 'GET':
		form = addProductosForm(instance = objetoProd)
	else:
		form = addProductosForm(request.POST, instance=objetoProd)
		if form.is_valid():
			form.save()
		return redirect('productos:listaProductos')
	return render(request, 'forms/nuevoProductoForm.html',{'form':form})

def producto_delete(request, id_Prod):
	objetoProd = Producto.objects.get(id_Prod = id_Prod)
	if request.method == 'POST':
		objetoProd.delete()
		return redirect('productos:listaProductos')
	return render(request, 'forms/producto_delete.html',{'producto':objetoProd})





# ALTAS, BAJAS, CAMBIOS ----CATEGORIAS

def categorias_view(request):
	if request.method == 'POST':
		form = addCategoriasForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/index/categorias')
	else:
		form = addCategoriasForm()
	return render(request, 'forms/nuevaCategoriaForm.html', {'form':form})

def categoria_edit(request, id_Cat):
	objetoCat = Categoria.objects.get(id_Cat = id_Cat)
	if request.method == 'GET':
		form = addCategoriasForm(request.POST, instance=objetoCat)
		if form.is_valid():
			form.save()
		return redirect('/index/categorias')
	return render(request, 'forms/nuevaCategoriaForm.html',{'form':form})

def categoria_delete(request, id_Cat):
	objetoCat = Categoria.objects.get(id_Cat = id_Cat)
	if request.method == 'POST':
		objetoCat.delete()
		return redirect('/index/categorias')
	return render(request, 'forms/categoria_delete.html',{'categoria':objetoCat})