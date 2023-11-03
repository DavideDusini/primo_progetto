from django.urls import path
from prova_pratica_1.views import *
app_name="prova_pratica_1"

urlpatterns = [
    path("view_a", somma, name="view_a"),
    path("view_b", media, name="view_b"),
    path("view_c", voti, name="view_c"),
    path("",index, name="index_prova")
]
