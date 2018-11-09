from django.urls import path
from Productos.views import index,productos,categorias,nuevoRegistroProd,editarRegistroProd

app_name = 'productos'

# {}

urlpatterns = [
	path('index',index),
 #    path('index', index,name = "plantilla"),
 #    path('productos',productos,name= "listaProductos"),
 #    path('categorias',categorias),
 #    # path('categoriasv',viewProductos.as_view()),
 #    path('nuevoRegistroProd',nuevoRegistroProd,name="nuevoRegistroProd"),
	# path('editarRegistroProd/<prodId>',editarRegistroProd,name="editarRegistroProd"),
	# path('eliminarRegistroProd/<prodId>',eliminarRegistroProd,name="eliminarRegistroProd"),
    

]