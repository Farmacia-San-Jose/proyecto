# API
from rest_framework import serializers

# MODELS
from apps.locations.models import Ubicacion, Seccion, HistorialInvetario

# SERIALIZER
from apps.medicines.api.serializer import MedicamentoSerializer


class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'

class HistorialInvetarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HistorialInvetario
        fields = '__all__'
""" 
    def to_representation(self, instance):
        return {
            'id':instance.id,

            'medicine_id':{
                'id':instance.medicine_id.id,
                'medicine_name':instance.medicine_id.medicine_name,
                'description':instance.medicine_id.description

            },

            'location_id':{
                'id':instance.location_id,
                'type_location':instance.location_id.type_location,

            },

            #'quantity_stock':instance.quantity_stock,
            #'row':instance.row,
            #'column':instance.column,
            #'sale_price':instance.sale_price,
            #'locationsection_id':{
             #   'id':instance.locationsection_id.id,
              #  'location_section':instance.locationsection_id.location_section
            #}
        }
        """