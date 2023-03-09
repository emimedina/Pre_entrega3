from django.db import models

# Create your models here.
class Usuarios(models.Model):
    #id = models.AutoField(primary_key=)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Compras(models.Model):
    articulo = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    comprador = models.CharField(max_length=30)

class Productos(models.Model):
    producto = models.CharField(max_length=30)
    cantidad_disponible = models.IntegerField()
    precio = models.IntegerField()