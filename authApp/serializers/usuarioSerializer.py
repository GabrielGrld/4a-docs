from rest_framework                         import serializers
from authApp.models.usuario                 import User
from authApp.models.account                 import Account
from authApp.serializers.accountSerializer  import AccountSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'usuario_nombre','usuario_telefono','usuario_tipo_id',
        'usuario_numero_id', 'usuario_ciudad', 'usuario_direccion', 'password','usuario_email',
        'account']

    def create(self, validated_data):
            accountData = validated_data.pop('account')
            userInstance = User.objects.create(**validated_data)
            Account.objects.create(user=userInstance, **accountData)
            return userInstance

    def to_representation(self, obj):
            user = User.objects.get(id=obj.id)
            account = Account.objects.get(user=obj.id) 
            return {
                'id': user.id,
                'username': user.username,
                'usuario_nombre': user.usuario_nombre,
                'usuario_telefono': user.usuario_telefono,
                'usuario_tipo_id': user.usuario_tipo_id,
                'usuario_numero_id': user.usuario_numero_id,
                'usuario_ciudad': user.usuario_ciudad,
                'usuario_direccion': user.usuario_direccion,
                'password': user.password,
                'usuario_email': user.usuario_email,
                
                'account': {
                    'id': account.id,
                    'lastChangeDate': account.lastChangeDate,
                    'isActive': account.isActive
            }
        }
