from django.db import models

# Create your models here.
# centre/models.py
from django.db import models

class Rol(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Usuari(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    assignatures = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nom} {self.cognom}'
