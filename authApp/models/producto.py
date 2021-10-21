from django.db import models


class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    prod_categoria = models.CharField('Categoria', max_length = 40, unique=False, default='null')
    prod_referencia = models.CharField('Referencia', max_length = 45, unique=False,default='null')
    prod_precio = models.IntegerField('Precio', unique=False, default=0)
    prod_descripcion = models.TextField ('Descripción', unique=False,default='null')