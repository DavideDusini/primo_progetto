from django.urls import path
from .views import home,articoloDetailView

app_name="news"

urlpatterns=[
    path('home_articolo', home, name="home"),
    path('articoli/<int:pk>',articoloDetailView, name="articolo_detail")
]