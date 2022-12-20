from django.db import models

# Create your models here.


class animal(models.Model):
    nombre= models.CharField(max_length=50)
    especie=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} - {str(self.especie)}"

class doctor(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return f"{self.nombre} - {str(self.apellido)}"

class veterinaria(models.Model):
    nombre= models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre}"
