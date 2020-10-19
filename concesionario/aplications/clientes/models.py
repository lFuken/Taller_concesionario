from django.db import models

# Create your models here.
class Cliente(models.Model):#creo tabla llamada Departamentos
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=50)
    direccion_cliente = models.CharField(max_length=50)
    poblacion = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return str(self.id)+ '-' + self.nombre_cliente + '-' + self.apellido_cliente + '-' + self.direccion_cliente + '-' + self.poblacion + '-' + self.codigo_postal + '-' + self.provincia + '-' + self.telefono + '-' + str(self.fecha_nacimiento)