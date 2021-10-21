from django.conf import settings
from django.db.models import query
from django.http import request
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated


from authApp.models import Factura
from authApp.serializers import FacturaSerializer


class FacturaCreateView(generics.CreateAPIView):
    serializer_class = FacturaSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        serializer = FacturaSerializer(
            data=request.data['factura_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("creacion exitosa de factura", status=status.HTTP_201_CREATED)


class FacturaDetailView(generics.RetrieveAPIView):
    serializer_class = FacturaSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Factura.objects.all()

    def get(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)

class FacturaUpdateView(generics.UpdateAPIView):
    serializer_class = FacturaSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Factura.objects.all()

    def update(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().update(request, *args, **kwargs)

class FacturaDeleteView(generics.DestroyAPIView):
    serializer_class = FacturaSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Factura.objects.all()

    def delete(self, request, *args, **kwargs):

        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().destroy(request, *args, **kwargs)

