from authApp.models.producto import Producto
from authApp.models.usuario import User
from authApp.models.factura import Factura
from rest_framework  import serializers

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura 
        fields = ['id','user','producto','factura_fecha','direccion_envio',
        'metodo_pago','valor_envio','valor_producto','valor_impuesto','subtotal','valor_total']
    
    def to_representation(self, instance):
        user = User.objects.get(id = instance.user_id)
        producto = Producto.objects.get(id = instance.producto_id)
        factura = Factura.objects.get(id = instance.id)

        return {
            'factura_numero':factura.id,
            'user':{
                'id': user.id,
                'name': user.username,
                'email': user.usuario_email
            },
            'producto':{
                 'prod_serial': producto.id,
                 'prod_referencia':producto.prod_referencia,
                 'prod_precio':producto.prod_precio
            },
            'factura_fecha':factura.factura_fecha,
            'direccion_envio': factura.direccion_envio,
            'metodo_pago':factura.metodo_pago,
            'valor_envio':factura.valor_envio,
            'valor_producto':factura.valor_producto,
            'valor_impuest': factura.valor_impuesto,
            'subtotal': factura.subtotal,
            'valor_total': factura.valor_total
            }
        
      