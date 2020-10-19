from django.db import models
from aplications.clientes.models import Cliente
# Create your models here.

class Coche(models.Model):
    MARCA_CHOISES = {
        ('0','CHEVROLET'),
        ('1','KIA'),
        ('2','HYUNDAI'),
        ('3','MERCEDES'),
        ('4','OTRO'),
    }
    matricula= models.CharField(max_length=100, primary_key=True)
    marca = models.CharField('Marca', max_length=1, choices=MARCA_CHOISES)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    precio = models.IntegerField()
    numero_de_puertas = models.CharField(max_length=50)
    extras_instalados = models.CharField(max_length=50)
    codigo_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.matricula + '-' + self.marca + '-' + self.modelo + '-' + self.color + '-' + str(self.precio) + '-' + self.numero_de_puertas + '-' + self.extras_instalados
