from django.urls import path
from .views import *

app_name="news"

urlpatterns=[
    path('home_articolo', home, name="home"),
    path('articoli/<int:pk>',articoloDetailView, name="articolo_detail"),
    path('lista_articoli/<int:pk>',listaArticoli, name="lista_articoli_giornalista"),
    path('lista_articoli/',listaArticolo, name="lista_articolo"),
    path('query_base',queryBase, name="query_base"),
    path('',index,name='index_news'),
    path('giornalisti/<int:pk>', giornalistaDetailView, name="giornalista_detail")
]