from django.db import models
#se comunica c la base de datos
# Create your models here.

class Curso(models.Model):

    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()
