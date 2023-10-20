"""
URL configuration for pharmacy_sanjose project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# URL
from django.contrib import admin
from django.urls import path, include

# DECORADOR
from django.contrib.auth.decorators import login_required

# API
from rest_framework.documentation import include_docs_urls

# VIEWS
from . import views

# CONFIGURANCION PARA MANEJAR LOS STATICS Y MEDIA
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('accounts/login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'), 
    path('admin/', admin.site.urls),
    path('users/',include('apps.users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('medicamentos/',include('apps.medicines.urls')),
    path('docs/', include_docs_urls(title='DOCUMENTACION API')),
    path('clasificacion/', include('apps.classifications.urls')),
    path('ubicacion/',include('apps.locations.urls')),
    path('presentacion/',include('apps.presentations.urls')),
    path('proveedor/',include('apps.suppliers.urls')),
    path('transaccion/',include('apps.transactions.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
