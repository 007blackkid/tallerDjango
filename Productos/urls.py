from django.urls import path
from django.conf.urls import url
from Productos.views import index,productos,ventas,categorias,productos_view,producto_edit,producto_delete,categorias_view,categoria_edit,categoria_delete,alCarrito,deleteCarrito,pagarTODO
from django.views.generic import RedirectView

app_name = 'productos'

# {}

urlpatterns = [	
	path('',index, name= "index"),    
    path('productos',productos,name= "listaProductos"),
    path('categorias',categorias,name= "listaCategorias"),
    path('ventas',ventas, name = "listaVentas"),

    # PRODUCTOS ALTAS, BAJAS Y CAMBIOS
    path('productos/productos_view',productos_view),
    url('productos/editar/(?P<id_Prod>\d+)/$', producto_edit, name = 'producto_editar'),
    url('productos/eliminar/(?P<id_Prod>\d+)/$', producto_delete, name = 'producto_eliminar'),

    # CATEGORIAS ALTAS, BAJAS Y CAMBIOS
    path('categorias/categorias_view',categorias_view),
    url('categorias/editar/(?P<id_Cat>\d+)/$', categoria_edit, name = 'categoria_editar'),
    url('categorias/eliminar/(?P<id_Cat>\d+)/$', categoria_delete, name = 'categoria_eliminar'), 

    # VENTAS AÑADIR AL CARRITO, ELIMINAR DEL CARRITO
    url('ventas/add/(?P<id_Prod>\d+)/$', alCarrito  , name = 'adlCarrito'),
    url('ventas/del/(?P<id_Venta>\d+)/$', deleteCarrito  , name = 'delCarrito'),
    url('ventas/pagarTODO',pagarTODO, name = "pagar"),
    

]



