# URL
from django.urls import path, include

# API
from apps.users.api import routers
# VIEWS
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [
    path('',views.userListView.as_view(),name='index'),
    path('create', views.userCreateView.as_view(), name='createuser'),
    path('update/<int:pk>', views.userUpdateView.as_view(), name='updateuser'),
    path('delete/<int:pk>', views.userDeleteView.as_view(), name='deleteuser'),
]

urlpatterns+= routers.urlpatterns
