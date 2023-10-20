# URL
from django.urls import path, include

# VIEWS
from . import views

# API
from .api import routers

urlpatterns = [
    path('api/v1/',include(routers.router.urls))
    
]
