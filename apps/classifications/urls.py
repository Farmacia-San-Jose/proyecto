# URL
from django.urls import path, include

# VIEWS
from . import views

# API
from .api import routers

app_name = 'classifications'

urlpatterns = [
    path('api/v1/',include(routers.router.urls)),
    path('agregar/',views.agregar_uso, name='agregar')
    
]
