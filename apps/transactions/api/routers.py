# URL
from django.urls import path, include

# API
from rest_framework import routers

# VIEWS
from . import views

# API ROUTERS
router = routers.DefaultRouter()
router.register(r'historial-transaccion', views.HistorialTransaccionViewSet, 'historial-transaccion')
router.register(r'detalle-transaccion', views.DetalleTransaccionViewSet, 'detalle-transaccion')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/v1/transaccion/',views.HistorialTransaccionList.as_view(),name='transaction-list'),
    path('api/v1/transaccion/<int:pk>/',views.HistorialTransaccionDetail.as_view(),name='transaction-detail'),
    path('api/v1/transaccion/detalle/', views.DetailTransaccionList.as_view(), name='detail-transaccion'),
    path('api/v1/transaccion/detail/<int:pk>/',views.DetailTransaccionDetail.as_view(), name='detail-transaccionDetail'),

]