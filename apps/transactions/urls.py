# URL
from django.urls import path, include

# VIEWS
from . import views

# API
from apps.transactions.api import routers

app_name = 'transactions'

urlpatterns = [
    path('realizar_transaccion/', views.agregar_transaccion, name='realizar_transaccion')


]

urlpatterns+=routers.urlpatterns