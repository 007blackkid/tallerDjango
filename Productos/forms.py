from django import forms
from Productos.models import Producto

class ProductosForm(forms.ModelForm):

	class Meta:
		model = Producto
		fields =[
				'prodNombre',
				'prodDescripcion',
				'prodPrecio',
				'prodDisponible',
				'prodExistencias',
				'prodCatId',
		]

		labels = {
				'prodNombre' : 'Nombre',
				'prodDescripcion': 'Descripcion',
				'prodPrecio' : 'Precio',
				'prodDisponible': 'Disponible',
				'prodExistencias' :  'Existencias',
				'prodCatId': 'Categoria',
		}

		widgets = {
		'prodNombre' : forms.TextInput(attrs={}),
		'prodDescripcion' : forms.TextInput(),
		'prodPrecio' : forms.TextInput(),
		'prodDisponible': forms.TextInput(),
		'prodExistencias' : forms.TextInput(),
		'prodCatId' : forms.TextInput(),
		}