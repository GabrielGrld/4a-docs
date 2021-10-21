"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views
from authApp.models.producto import Producto
from authApp.views import userDeleteView
from authApp.views import userUpdateView
from authApp.views.productoView import ProductoDeleteView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('user/delete/<int:pk>/',views.UserDeleteView.as_view()),
    path('user/update/<int:pk>/',views.UserUpdateView.as_view()),

    #URL´s de producto
    path('productos/all/', views.ProductoView.as_view()), #ver todos los productos
    path('productos/filtered/<int:pk>/', views.ProductoFilteredView.as_view()), #ver productos filtrados 
    path('productos/create/', views.ProductoCreateView.as_view()), #crear un producto
    path('productos/delete/<int:pk>/', views.ProductoDeleteView.as_view()), #borrar un producto
    path('productos/update/<int:pk>/', views.ProductoUpdateView.as_view()), #actializar un producto

    #URL´s de PQR
    path('pqr/create/', views.PqrCreateView.as_view()), #crear una PQR
    path('pqr/delete/', views.PqrDeleteView.as_view()), #borrar una PQR
    path('pqr/filtered/<int:user>/<int:pk>/', views.PqrDetailView.as_view()), #ver PRQ filtrada
    path('pqr/update/<int:user>/<int:pk>/', views.PqrUpdateView.as_view()), #actualizar una PQR
   
    #URLS para peticiones del modelo factura
     path('factura/create/', views.FacturaCreateView.as_view()),
     path('factura/detail/<int:user>/<int:pk>/', views.FacturaDetailView.as_view()),
     path('factura/update/<int:user>/<int:pk>/', views.FacturaUpdateView.as_view()),
     path('factura/delete/<int:user>/<int:pk>/', views.FacturaDeleteView.as_view()),
   
]
