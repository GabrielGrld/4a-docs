from django.conf                            import settings
from rest_framework                         import generics, status, views
from rest_framework.response                import Response
from rest_framework_simplejwt.backends      import TokenBackend
from rest_framework.permissions             import IsAuthenticated
from rest_framework_simplejwt.serializers   import TokenObtainPairSerializer, TokenObtainSerializer
from authApp.models.producto                import Producto
from authApp.serializers.productoSerializer import ProductoSerializer


#Crear un producto
class ProductoCreateView(views.APIView):
    
    def post (self, request, *args, **kwargs): #revisar
        
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        tokenData = {"prod_serial":request.data["prod_serial"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer.validated_data,status=status.HTTP_201_CREATED)
    

#Traer todos los productos
class ProductoView (generics.ListAPIView):
    queryset=Producto.objects.all()
    serializer_class=ProductoSerializer

#Traer un producto filtrado 
class ProductoFilteredView (generics.ListAPIView):
    serializer_class     = ProductoSerializer

    def get_queryset(self):
        queryset = Producto.objects.filter(prod_serial = self.kwargs['pk'])
        return queryset


