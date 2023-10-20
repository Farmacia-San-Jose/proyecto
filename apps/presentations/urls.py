# URL
from django.urls import path, include

# API
from apps.presentations.api import routers

# VIEWS
from . import views

urlpatterns = [
    
]

urlpatterns+=routers.urlpatterns