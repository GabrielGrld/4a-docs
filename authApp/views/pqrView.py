from django.conf                            import settings
from rest_framework                         import generics, status
from rest_framework.response                import Response
from rest_framework_simplejwt.backends      import TokenBackend
from rest_framework.permissions             import IsAuthenticated

from authApp.models.pqr                     import Pqr
from authApp.serializers.pqrSerializer      import PqrSerializer
from rest_framework                         import views
from rest_framework.response                import Response
from rest_framework_simplejwt.serializers   import TokenObtainPairSerializer
from authApp.serializers.usuarioSerializer  import UsuarioSerializer


#Crear una PQR
class PqrCreateView (generics.CreateAPIView):
    serializer_class    = PqrSerializer
    permission_classes  = (IsAuthenticated,)

    def post(self, request,*args, **kwargs):  #se quito el diccionario (revisar)
        serializer = PqrSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        tokenData = {"username":request.data["username"],
        "pqr_id":request.data["pqr_id"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
    
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

#Consultar todas las PQR
class PqrConsultView (generics.RetrieveAPIView):
    queryset            = Pqr.objects.all()
    serializer_class    = PqrSerializer
    permission_classes  = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)

#Consultar una PQR
class PqrFilteredView (generics.ListAPIView):
    serializer_class     = PqrSerializer
    permission_classes   = (IsAuthenticated,)

    def get_queryset(self):
        token           = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend    = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data      = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Pqr.objects.filter(pqr_id = self.kwargs['pqr_id'])
        return queryset

#Actualizar una PQR
class PqrUpdateView (generics.UpdateAPIView):
    serializer_class     = PqrSerializer
    permission_classes   = (IsAuthenticated,)
    queryset             = Pqr.objects.all()

    def update(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().update(request, *args, **kwargs)

#Eliminar una PQR
class PqrDeleteView (generics.DestroyAPIView):
    serializer_class     = PqrSerializer
    permission_classes   = (IsAuthenticated,)
    queryset             = Pqr.objects.all()

    def delete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().delete(request, *args, **kwargs)
