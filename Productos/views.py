from django.shortcuts import render,redirect
from django.http import HttpResponse
from Productos.models import Categoria,Producto
from Productos.forms import ProductosForm

def index(request):
 	return render(request,'base/index.html')

def consolas(request):	
	# consolas_list = Producto.objects.get(prodCatId=1)
	consolas_list = Producto.objects.all()
	contexto = {'consolas_list':consolas_list}
	return render(request,'tienda/consolas.html', contexto)

def juegos(request):
 	return render(request,'tienda/juegos.html')

def accesorios(request):
 	return render(request,'tienda/accesorios.html')

def ventas(request):
 	return render(request,'tienda/ventas.html')





 	

# def plantilla(request):
# 	return render(request,'base/index.html')

# def categorias(request):
# 	contexto = {
# 		'Categoria' : Categoria.objects.all()
# 	}
# 	return render(request,'tienda/categorias.html',contexto)

# def productos(request):
# 	contexto = {
# 		'Producto' : Producto.objects.all()
# 	}
# 	return render(request,'tienda/productos.html',contexto)


# def nuevoRegistroProd(request):
# 	if request.method == 'POST':
# 		form = ProductosForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('productos:listaProductos')
# 	else:
# 		form = ProductosForm()	
# 	return render (request, 'tienda/productoformulario.html',{'form':form})

# def editarRegistroProd(request,idProducto):
# 	Producto = Producto.objects.get(id=idProducto)
# 	if(request.method == 'GET'):
# 		form = ProductosForm(instance = Producto)
# 	else:
# 		form = ProductosForm(request.POST, instance=Producto)
# 		if( form.is_valid()):
# 			form.save()
# 			return redirect('productos:listaProductos')
# 	return render(request, 'tienda/productoformulario.html',{'form':form})

# def eliminarRegistroProd(request, prodId):
	
# class viewProductos(ListView):
# 	model =  Producto
# 	queryset = Producto.objects.filter(prodNombre = 'Producto1')
# 	template_name = 'tienda/productos.html'

# class viewClientes(listView):
# 	model = Categoria
# 	template = 'c/paginaEspecial.html'
