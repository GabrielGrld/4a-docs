from django.conf                            import settings
from rest_framework                         import generics, serializers, status
from rest_framework.response                import Response
from rest_framework_simplejwt.backends      import TokenBackend
from rest_framework.permissions             import IsAuthenticated

from authApp.models.factura                   import Factura
from authApp.serializers.facturaSerializer    import FacturaSerializer

#crear un factura
class FacturaCreateView (generics.CreateAPIView):
    serializers         = FacturaSerializer
    permission_classes  = (IsAuthenticated,)

    def post(self, request, *args, **kwargs): #revisar
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        serializer = FacturaSerializer(data=request.data['factura_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Factura creado", status=status.HTTP_201_CREATED)

#Consultar factura 
class FacturaFilteredView (generics.ListAPIView):
    serializer_class     = FacturaSerializer
    permission_classes   = (IsAuthenticated,)

    def get_queryset(self):
        token           = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend    = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data      = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Factura.objects.filter(envio_id = self.kwargs['envio_id'])
        return queryset

