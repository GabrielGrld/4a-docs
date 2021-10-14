from authApp.models.pqr import Pqr
from rest_framework import serializers
from authApp.models.usuario import User
from authApp.serializers.usuarioSerializer import UsuarioSerializer

class PqrSerializer(serializers.ModelSerializer):
    user= UsuarioSerializer()
    class Meta:
        model = Pqr
        fields = ['pqr_tipo_solicitud', 'pqr_clasificacion','pqr_descripcion','pqr_estado','user']
    def create(self, validated_data): 
        userData = validated_data.pop('usuario')
        pqrInstance = Pqr.objects.create(**validated_data)
        User.objects.create(pqr=pqrInstance, **userData)
        return pqrInstance
    def to_representation(self, obj):
        pqr = Pqr.objects.get(pqr_id=obj.pqr_id)
        user = User.objects.get(pqr=obj.pqr_id) 
        return {   #campos de pqr nativos
            'pqr_tipo_solicitud': pqr.pqr_tipo_solicitud,
            'pqr_clasificacion': pqr.pqr_clasificacion,
            'pqr_descripcion': pqr.pqr_descripcion,
            'pqr_estado': pqr.pqr_estado,
            'user': { #datos de campo usuario cambiar
                'id': user.id,
                'username': user.username,
                'usuario_nombre': user.usuario_nombre,
                'usuario_email': user.usuario_email
            }
 }