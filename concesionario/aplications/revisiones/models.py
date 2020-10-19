from django.db import models
from aplications.coches_vendidos.models import Coche
# Create your models here.

class Revision(models.Model):#creo tabla llamada Departamentos

    CHOISES = {
        ('0','SI'),
        ('1','NO'),
    }

    Cambio_aceite = models.CharField('Cambio aceite', max_length=1, choices=CHOISES)
    Cambio_filtro = models.CharField('Cambio filtro', max_length=1, choices=CHOISES)
    revicion_frenos = models.CharField('revicion frenos', max_length=1, choices=CHOISES)
    matricula_coche = models.ForeignKey(Coche, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)+ '-' + self.Cambio_aceite + '-' + self.Cambio_filtro + '-' + self.revicion_frenos