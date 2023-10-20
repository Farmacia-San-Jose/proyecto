
# API
from rest_framework import serializers

# MODELO
from apps.medicines.models import Medicamento, HistorialMedicamento

# SERIALIZER
from apps.suppliers.api.serializer import ProveedorSerializer
from apps.presentations.api.serializer import PresentacionSerializer

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'


class HistorialMedicamentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialMedicamento
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'medicine_id':{
                'id':instance.medicine_id.id,
                'medicine_name':instance.medicine_id.medicine_name,
                'description':instance.medicine_id.description,
                'creation_date':instance.medicine_id.creation_date   
            },
            'supplier_id':{
                'id':instance.supplier_id.id,
                'first_name':instance.supplier_id.first_name,
                'last_name':instance.supplier_id.last_name,
                'company':instance.supplier_id.company,
                'email':instance.supplier_id.email,
                'telephone':instance.supplier_id.telephone
            },
            'presentation_id':{
                'id':instance.presentation_id.id,
                'presentation_type':instance.presentation_id.presentation_type,
                'description':instance.presentation_id.description
            },
            'cost_price':instance.cost_price,
            'brand':instance.brand,
            'medication_code':instance.medication_code,
            'expiration_date':instance.expiration_date

        }