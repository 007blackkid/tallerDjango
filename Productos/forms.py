from django import forms
from Productos.models import Producto,Categoria


class addProductosForm(forms.ModelForm):

	
	class Meta:		
		model = Producto
		fields =[
				'Nombre',
				'Descripcion',
				'Precio',				
				'Existencias',
				'CatId',
		]

		labels = {
			'Nombre': 'Nombre',
			'Descripcion': 'Descripcion',
			'Precio' : 'Precio',				
			'Existencias' : 'Existencias',
			'CatId' : 'Categoria',
		}

		widgets = {
			'Nombre': forms.TextInput(),
			'Descripcion': forms.TextInput(),
			'Precio' : forms.TextInput(),				
			'Existencias' : forms.TextInput(),
			'CatId' : forms.Select(),
		}

class addCategoriasForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields =[
			'catNombre',
		]

		labels = {
			'catNombre': 'Nombre',
		}


		widgets = {
			'catNombre': forms.TextInput(),
		}
