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
    path('giornalisti/<int:pk>', giornalistaDetailView, name="giornalista_detail"),
    path('giornalisti_list_api', giornalisti_list_api, name="giornalisti_list_api"),
    path('giornalista_api/<int:pk>', giornalista_api, name="giornalista_api"),
    path('articoli_list_api', articoli_list_api, name="articoli_list_api"),
    path('articoli_api/<int:pk>', articoli_api, name="articoli_api"),
    path('json1',json1,name="json1"),
    path('json2',json2,name="json2"),
]