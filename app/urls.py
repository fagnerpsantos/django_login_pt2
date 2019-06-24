from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('logar_usuario', logar_usuario, name="logar_usuario"),
    path('deslogar_usuario', deslogar_usuario, name="deslogar_usuario"),
    path('alterar_senha/', alterar_senha, name='alterar_senha'),
    path('cadastrar_usuario', cadastrar_usuario, name="cadastrar_usuario"),
    path('index', index, name="index"),
]