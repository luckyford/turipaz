from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
]