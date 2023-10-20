# URL
from django.urls import path, include

# API
from rest_framework import routers

# VIEWS
from . import views

# API ROUTERS
router = routers.DefaultRouter()
router.register(r'proveedor', views.ProveedorViewSet, 'proveedor')

urlpatterns = [
    path('api/', include(router.urls)),
    #path('api/v1/',views.ProveedorList.as_view(),name='proveedor-list'),
    #path('api/v1/<int:pk>/',views.ProveedorDetail.as_view(),name='proveedor-detail'),
]
