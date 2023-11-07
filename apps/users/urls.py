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
    path('',login_required(views.userListView.as_view()),name='index'),
    path('create', login_required(views.userCreateView.as_view()), name='createuser'),
    path('update/<int:pk>', login_required( views.userUpdateView.as_view()), name='updateuser'),
    path('delete/<int:pk>', login_required(views.userDeleteView.as_view()), name='deleteuser'),
    path('perfil/', views.perfil, name="perfil"),
]

urlpatterns+= routers.urlpatterns
