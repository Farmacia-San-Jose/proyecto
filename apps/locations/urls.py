# URL
from django.urls import path, include

#API
from apps.locations.api import routers

# VIEWS
from . import views




urlpatterns = [
    
]

urlpatterns+=routers.urlpatterns