# URL
from django.urls import path, include

# API
from rest_framework import routers

# VIEWS
from . import views

# API ROUTERS
router = routers.DefaultRouter()
router.register(r'clasificacion',views.ClasificacionViewSet,'clasificacion')
router.register(r'uso-terapeutico',views.UsoTerapeuticoViewSet,'uso-terapeutico')
router.register(r'forma-administracion',views.FormaAdministracionViewSet,'forma-administracion')



