# URL
from django.urls import path, include

# API - ROUTERS
from rest_framework import routers


# VIEWS
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required



# API ROUTERS
router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('api/v1/', views.UserList.as_view(), name='user-list'),
    path('api/v1/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    
]
