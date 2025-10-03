from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
]
