from django.contrib import admin
from .models import Seccion, Ubicacion, HistorialInvetario
# Register your models here.

admin.site.register(Ubicacion)
admin.site.register(Seccion)
admin.site.register(HistorialInvetario)
