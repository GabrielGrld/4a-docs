from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from authApp.models.usuario import User
from authApp.serializers.usuarioSerializer import UsuarioSerializer
from django.http.response import JsonResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

class UserUpdateView (generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        try: 
            user = User.objects.get(id=kwargs['pk']) 
        except User.DoesNotExist: 
            return JsonResponse({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()    #verificar el guardado por si se hace con otro comando ...
            return JsonResponse(UsuarioSerializer.data) 

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().put(request, *args, **kwargs)