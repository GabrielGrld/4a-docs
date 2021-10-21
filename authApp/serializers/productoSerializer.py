from rest_framework import serializers
from authApp.models.producto import Producto


class ProductoSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Producto
        fields = ['id', 'prod_categoria', 'prod_referencia','prod_precio','prod_descripcion']
    