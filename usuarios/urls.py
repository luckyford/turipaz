from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.inicio_sesion, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('perfil/', views.ver_perfil, name='perfil'),
]