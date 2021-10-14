from authApp.models.factura import Factura
from rest_framework import serializers
from authApp.models.producto import Producto
from authApp.serializers.productoSerializer import ProductoSerializer
from authApp.models.usuario import User
from authApp.serializers.usuarioSerializer import UsuarioSerializer
class FacturaSerializer(serializers.ModelSerializer):
    user= UsuarioSerializer()
    producto=ProductoSerializer()
    class Meta:
        model = Factura
        fields = ['factura_numero', 'factura_fecha', 'direccion_envio', 'metodo_pago','valor_envio',
        'valor_producto','valor_impuesto','subtotal','valor_total','userproducto']
    def create(self, validated_data):
        infoData = validated_data.pop('userproducto')
        
        facturaInstance = Factura.objects.create(**validated_data)
        User.objects.create(factura=facturaInstance, **infoData)
        Producto.objects.create(factura=facturaInstance, **infoData)   #validar que esté bien
        return facturaInstance

    def to_representation(self, obj):
        factura = Factura.objects.get(factura_numero=obj.factura_numero)
        user = User.objects.get(factura=obj.factura_numero) 
        producto= Producto.objects.get(factura=obj.factura_numero) 
        return {   #campos de pqr nativos
            'factura_numero': factura.factura_numero,
            'factura_fecha' : factura.factura_fecha,
            'direccion_envio' : factura.direccion_envio,
            'metodo_pago' : factura.metodo_pago,
            'valor_envio' : factura.valor_envio,
            'valor_producto' : factura.valor_producto,
            'valor_impuesto' : factura.valor_impuesto,
            'subtotal' : factura.subtotal,
            'valor_total' : factura.valor_total,

            'userproducto': { #datos de campo usuario/detalle cambiar
                'id': user.id,
                'prod_serial': producto.prod_serial
            }
            
 }