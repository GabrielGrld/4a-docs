from django.db import models
from .usuario import User
from .producto import Producto

class Factura(models.Model):
    id     = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='usuarioFactura',on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='productoFactura',on_delete=models.CASCADE)

    factura_fecha= models.DateTimeField('Fecha de compra',auto_now_add=True,blank=True)
    direccion_envio = models.CharField('Direccion de envío', max_length = 80, unique=False, default='null')
    metodo_pago = models.CharField('Método de pago', max_length = 20, unique=False, default='null')
    valor_envio = models.IntegerField('valor de envío', unique=False, default='null')
    valor_producto = models.IntegerField('valor de producto', unique=False, default='null')
    valor_impuesto = models.IntegerField('valor de impuesto',  unique=False, default='null')
    subtotal = models.IntegerField('Subtotal',  unique=False, default='null')
    valor_total = models.IntegerField('valor total', unique=False, default='null')
