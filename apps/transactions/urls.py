# URL
from django.urls import path, include

# VIEWS
from . import views

# API
from apps.transactions.api import routers

urlpatterns = [


]

urlpatterns+=routers.urlpatterns