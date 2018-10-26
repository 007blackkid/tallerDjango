from django.db import models

class Categoria(models.Model):	
	idCat = models.AutoField(primary_key=True)
	catNombre = models.CharField(max_length=30,default = 'default')
	catFechaCreacion = models.DateField(default = '2018-09-08')

class Producto(models.Model):
	idProd = models.AutoField(primary_key=True)
	prodNombre = models.CharField(max_length=30)
	prodDescripcion = models.CharField(max_length=50)
	prodPrecio = models.DecimalField(max_digits=5,decimal_places=2,default = 0)
	prodDisponible = models.BooleanField(default ='false')
	prodExistencias = models.IntegerField(default = 0)	
	prodCatId = models.ForeignKey(Categoria,default = '1',on_delete = models.CASCADE)
		
