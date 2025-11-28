from django.db import models

class Articulo(models.Model):
    tipo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to= 'productos',null=True, blank=True)

    def __str__(self):
        return f'Articulo ({self.pk}): {self.tipo} - {self.marca}'