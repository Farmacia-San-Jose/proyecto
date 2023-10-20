from django.contrib import admin
from .models import HistorialTransaccion, DetalleTransaccion

# Register your models here.
admin.site.register(HistorialTransaccion)
admin.site.register(DetalleTransaccion)