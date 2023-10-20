# URL
from django.urls import path, include

# API
from apps.suppliers.api import routers

# VIEWS
from . import views

urlpatterns = [
    
]

urlpatterns+= routers.urlpatterns