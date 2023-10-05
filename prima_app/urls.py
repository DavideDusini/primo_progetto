from django.urls import path
from prima_app.views import homapage, welcome, lista, chi_siamo, variabili

app_name="prima_app"
urlpatterns=[
    path('', homapage, name='homepage'),
    path('welcome', welcome, name='welcome'),
    path('lista',lista,name='lista'),
    path('chi_siamo', chi_siamo, name='chi_siamo'),
    path('variabili',variabili,name='variabili')
    ]