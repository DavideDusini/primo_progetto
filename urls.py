from django.urls import path
from primo_progetto.views import index_root

app_name="primo_progetto"
urlpatterns=[
    
    path('',index_root,name='index_root')
    ]