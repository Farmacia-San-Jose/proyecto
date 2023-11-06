# URL
from django.urls import path, include

# API
from apps.suppliers.api import routers

# VIEWS
from apps.suppliers import views

app_name = 'suppliers'

urlpatterns = [
    path('',views.provListView.as_view(),name='index'),
    path('create', views.provCreateView.as_view(), name='createprov'),
    path('update/<int:pk>', views.provUpdateView.as_view(), name='updateprov'),
    path('delete/<int:pk>', views.provDeleteView.as_view(), name='deleteprov'),
]

urlpatterns+= routers.urlpatterns