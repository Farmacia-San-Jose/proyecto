# URL
from django.urls import path, include

# VIEWS
from . import views

# API
from apps.transactions.api import routers

app_name = 'transactions'

urlpatterns = [
    path('realizar_transaccion/', views.agregar_transaccion, name='realizar_transaccion'),
    path('', views.listar_transacciones, name='index'),
    path('detalle/<int:id>/', views.detalle_transaccion, name='detalle'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('editar/<int:id>/', views.editar_transacciones, name='editar'),


]

urlpatterns+=routers.urlpatterns