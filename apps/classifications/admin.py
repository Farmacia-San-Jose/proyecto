from django.contrib import admin
from .models import Clasificacion, UsoTerapeutico, FormaAdministracion

# Register your models here.
admin.site.register(Clasificacion)
admin.site.register(UsoTerapeutico)
admin.site.register(FormaAdministracion)
