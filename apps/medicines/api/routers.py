# URL
from django.urls import path, include

# API
from rest_framework import routers
# from rest_framework.urlpatterns import format_suffix_patterns


# VIEWS
from . import views

# API ROUTERS
router = routers.DefaultRouter()
router.register(r'medicamentos', views.MedicamentoViewSet,'medicamentos')
router.register(r'historial-medicamento',views.HistorialMedicamentoViewSet,'historial-medicamento')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/v1/medicamento/', views.MedicamentoList.as_view(), name='medicamento-list'),
    path('api/v1/medicamento/<int:pk>/',views.MedicamentoDetail.as_view(), name='medicamento-detail'), 
    path('api/v1/historial-medicamento/',views.HistorialMedicamentoList.as_view(),name='historial-medicamento'),
    path('api/v1/historial-medicamento/<int:pk>',views.HistorialMedicamentoDetail.as_view(),name='historial-medicamentoDetail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)