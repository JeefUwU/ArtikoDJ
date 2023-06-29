from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
	usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

class Product(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    digital = models.BooleanField(default=True,null=False, blank=True)


    def __str__(self):
        return self.nombre
    
class Orden(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
	fecha_orden = models.DateTimeField(auto_now_add=True)
	completado = models.BooleanField(default=False)
	transaccion_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.transaccion_id)
	

class OrdenItem(models.Model):
	producto = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True)
	cantidad = models.IntegerField(default=0, null=True, blank=True)
	fecha_agregada = models.DateTimeField(auto_now_add=True)
	
class DireccionPedido(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
	orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True)
	direccion = models.CharField(max_length=200, null=False)
	ciudad = models.CharField(max_length=200, null=False)
	estado = models.CharField(max_length=200, null=False)
	codigopostal = models.CharField(max_length=200, null=False)
	fecha_agregada = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.direccion