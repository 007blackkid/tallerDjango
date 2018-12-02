from django.db import models

class Categoria(models.Model):	
	id_Cat = models.AutoField(primary_key = True)
	catNombre = models.CharField(max_length=30,default = 'Nombre_Default')
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	catStatus = models.BooleanField(default=True)

	def __str__(self):
		return '{}'.format(self.catNombre)

class Producto(models.Model):
	id_Prod = models.AutoField(primary_key=True)
	Nombre = models.CharField(max_length=30)
	Descripcion = models.CharField(max_length=70)
	Precio = models.DecimalField(max_digits=8,decimal_places=2,default = 0)	
	Existencias = models.IntegerField(default = 0)	
	Status = models.BooleanField(default=True)
	CatId = models.ForeignKey(Categoria,default = '1',on_delete = models.CASCADE)

	def __str__(self):
		return '{''}'.format(self.Nombre)

class Venta(models.Model):
	id_Venta = models.AutoField(primary_key=True)
	Nombre = models.CharField(max_length=30)
	Precio = models.DecimalField(max_digits=8,decimal_places=2,default = 0)	
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	
	

	


		
