from django.conf import settings
from django.db.models import query
from django.http import request
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models import Pqr
from authApp.serializers import PqrSerializer


class PqrCreateView(generics.CreateAPIView):
    serializer_class = PqrSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        serializer = PqrSerializer(
            data=request.data['pqr_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("creacion exitosa de solicitud PQR", status=status.HTTP_201_CREATED)


class PqrDetailView(generics.RetrieveAPIView):
    serializer_class = PqrSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Pqr.objects.all()

    def get(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)


class PqrUpdateView(generics.UpdateAPIView):
    serializer_class = PqrSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Pqr.objects.all()

    def update(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().update(request, *args, **kwargs)

class PqrDeleteView(generics.DestroyAPIView):
    serializer_class = PqrSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Pqr.objects.all()

    def delete(self, request, *args, **kwargs):

        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().destroy(request, *args, **kwargs)

