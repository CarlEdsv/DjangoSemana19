from django.db import models
from django.contrib.auth.models import Group

#Tabla de proveedores
class Proveedores(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre

#Tablal de productos
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    fk_prov = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


#Se crean dos grupos, uno de Cajero, y otro de estudiante
Group.objects.get_or_create(name='Cajero')
Group.objects.get_or_create(name='Estudiante')

