# URL
from django.urls import path, include

# API
from rest_framework import routers

# VIEWS
from . import views

# API - ROUTES
router = routers.DefaultRouter()
router.register(r'historial_inventario',views.HistorialInventarioViewSet,'historial_inventario')
router.register(r'ubicacion', views.UbicacionViewSet, 'ubicacion')
router.register(r'seccion',views.SeccionViewSet,'seccion')


urlpatterns = [
    path('api/v1/',include(router.urls)),
    path('api/v1/historial-inventario/',views.HistorialInvetarioList.as_view(),name='historial-inventario'),
    path('api/v1/historial-inventario/<int:pk>/',views.HistorialInvetarioDetail.as_view(),name='historial-inventarioDetail')
]
