from django.db import models
from .usuario import User

class Pqr(models.Model):
    pqr_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='pqr', on_delete=models.CASCADE)
    pqr_tipo_solicitud = models.CharField('Tipo de Solicitud', max_length=45, help_text="Seleccione tipo de solicitud", unique=False)
    pqr_clasificacion = models.CharField('Clasificación',max_length=45, help_text="Seleccione clasificación de solicitud", unique=False)
    pqr_descripcion = models.TextField('Descripción', max_length=80, help_text="Describa su solicitud", unique=False)
    pqr_estado = models.CharField('Estado', max_length=45, unique=False)