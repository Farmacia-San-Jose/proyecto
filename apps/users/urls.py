# URL
from django.urls import path, include

# API
from apps.users.api import routers
# VIEWS
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required


urlpatterns = [
    
    
]

urlpatterns+= routers.urlpatterns
