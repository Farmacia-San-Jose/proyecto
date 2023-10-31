# URL
from django.urls import path, include

#API
from apps.locations.api import routers

# VIEWS
from . import views

app_name = 'locations'


urlpatterns = [
    path('medicamentos/<int:id>/',views.list_locations, name='listar_ubicacion')
    
]

urlpatterns+=routers.urlpatterns