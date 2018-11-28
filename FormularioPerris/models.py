from django.db import models

# Create your models here.
class Rescatado(models.Model):
    codigo = models.CharField(max_length=10)
    nombre =  models.CharField(max_length=30)
    tamano = models.CharField(max_length=30)
    peso = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    descripción = models.TextField()
    fechaRescate = models.DateField()
    op=(('R', 'Rescatado'),('D','Disponible'),('A','Adoptado'))
    estado= models.CharField(max_length=1, choices=op,default='R')

class Adoptante(models.Model):
    correo = models.CharField(max_length=60)
    run =  models.CharField(max_length=11)
    nombreCompleto = models.CharField(max_length=90)
    pefechaNacimiento = models.DateField()
    telefono = models.CharField(max_length=12)
    region = models.CharField(max_length=30)
    comuna = models.CharField(max_length=30)
    op=(('G', 'Casa con patio grande'),('P','Casa con patio pequeño'),('S','Casa sin patio'),('D','Departamento'))
    tipoVivienda= models.CharField(max_length=1, choices=op,default='G')