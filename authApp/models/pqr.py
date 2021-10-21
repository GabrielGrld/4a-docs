from django.db import models
from django.db.models.deletion import CASCADE
from .usuario import User


class Pqr (models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,related_name='usuarioPqr',on_delete=models.CASCADE)

    tipo = models.CharField(max_length= 50, default= 'null')
    clasificacion = models.CharField(max_length=45, default= 'null')
    estado = models.CharField(max_length=45,default='null')
    descripcion = models.TextField(default='null')
