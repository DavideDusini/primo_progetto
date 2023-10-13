from django.urls import path
from seconda_app.views import es_if

urlpatterns = [
    path("es_if", es_if, name="es_if")
]