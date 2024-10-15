from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AllaListor.as_view(), name='lista-hem'),
    path('lista/<int:pk>/', views.EnLista.as_view(), name='lista-sida'),
    path('lista/<int:pk>/Uppdatera', views.UppdateraLista.as_view(), name='lista-uppdatera'),
    path('lista/ny/', views.NyLista.as_view(), name='lista-ny'),
    path('vara/<int:pk>/ny/', views.NyVara.as_view(), name='vara-ny'),
]