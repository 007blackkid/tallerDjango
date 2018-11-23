from django.urls import path
from Productos.views import index,consolas,juegos,accesorios
from django.views.generic import RedirectView

app_name = 'productos'

# {}

urlpatterns = [	
	path('',index),    
    path('consolas',consolas),
    path('juegos',juegos),
    path('accesorios',accesorios),
 #    # path('categoriasv',viewProductos.as_view()),
 #    path('nuevoRegistroProd',nuevoRegistroProd,name="nuevoRegistroProd"),
	# path('editarRegistroProd/<prodId>',editarRegistroProd,name="editarRegistroProd"),
	# path('eliminarRegistroProd/<prodId>',eliminarRegistroProd,name="eliminarRegistroProd"),
    

]



