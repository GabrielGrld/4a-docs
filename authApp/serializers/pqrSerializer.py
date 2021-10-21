from authApp.models.usuario import User
from authApp.models.pqr import Pqr
from rest_framework import serializers


class PqrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pqr
        fields = ['id', 'user', 'tipo',
            'clasificacion', 'estado', 'descripcion']

    def to_representation (self, instance):
        user = User.objects.get(id = instance.user_id)
        pqr = Pqr.objects.get(id = instance.id)

        return{
            'pqr_id':pqr.id,
            'user':{
                'id': user.id,
                'name': user.username,
                'email': user.usuario_email
            },
            'tipo':pqr.tipo,
            'clasificacion': pqr.clasificacion,
            'estado': pqr.estado,
            'descripcion':pqr.descripcion
        }