from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from authApp.models.usuario import User
from authApp.serializers.usuarioSerializer import UsuarioSerializer
from django.urls import reverse_lazy

class UserDeleteView (generics.DestroyAPIView):
    serializer_class     = UsuarioSerializer
    permission_classes   = (IsAuthenticated,)
    queryset             = User.objects.all()

    def delete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().delete(request, *args, **kwargs)

    