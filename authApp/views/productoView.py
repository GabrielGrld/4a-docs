from django.conf                            import settings
from rest_framework                         import generics, status, views
from rest_framework.response                import Response
from rest_framework_simplejwt.backends      import TokenBackend
from rest_framework.permissions             import IsAuthenticated
from rest_framework_simplejwt.serializers   import TokenObtainPairSerializer, TokenObtainSerializer
from authApp.models.producto                import Producto
from authApp.serializers.productoSerializer import ProductoSerializer


#Crear un producto
class ProductoCreateView(generics.CreateAPIView):
    serializer_class   = ProductoSerializer
    permission_classes = (IsAuthenticated,)
    queryset=Producto.objects.all()

#Traer todos los productos
class ProductoView (generics.ListAPIView):

    queryset=Producto.objects.all()
    serializer_class=ProductoSerializer

#Traer un producto filtrado 
class ProductoFilteredView (generics.ListAPIView):
    serializer_class     = ProductoSerializer

    def get_queryset(self):
        queryset = Producto.objects.filter(id = self.kwargs['pk'])
        return queryset

#Eliminar un producto        
class ProductoDeleteView (generics.DestroyAPIView):
    serializer_class = ProductoSerializer
    permission_classes = (IsAuthenticated),
    queryset = Producto.objects.all()

    def delete(self, request, *args, **kwargs): 
        return super().destroy(request, *args, **kwargs) 

#Actualizar un producto 
class ProductoUpdateView(generics.UpdateAPIView):
    serializer_class   = ProductoSerializer
    permission_classes = (IsAuthenticated,)
    queryset=Producto.objects.all()
    