import django_filters
from apps.classifications.models import Clasificacion

class MedicineIdFiltro(django_filters.FilterSet):
    search = django_filters.CharFilter(field_name='medicine_id', lookup_expr='icontains')

    class Meta:
        model = Clasificacion
        fields  = ['search']