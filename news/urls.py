from django.urls import path
from .views import *

app_name="news"

urlpatterns=[
    path('home_articolo', home, name="home"),
    path('articoli/<int:pk>',articoloDetailView, name="articolo_detail"),
    path('lista_articoli/<int:pk>',listaArticoli, name="lista_articoli_giornalista"),
    path('lista_articoli/',listaArticolo, name="lista_articoli"),
]