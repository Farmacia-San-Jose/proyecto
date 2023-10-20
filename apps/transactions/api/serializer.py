# API
from rest_framework import serializers

# MODELS
from ..models import HistorialTransaccion,DetalleTransaccion

# SERIALIZADOR
from apps.users.api.serializers import UserSerializer
from apps.medicines.api.serializer import MedicamentoSerializer


class HistorialTransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialTransaccion
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'transaction':instance.transaction_type,
            'transaction_date':instance.transaction_date,
            'user_id':{
                'id':instance.user_id.id,
                'first_name':instance.user_id.first_name,
                'last_name':instance.user_id.last_name,
                'email':instance.user_id.email,
                'username':instance.user_id.email,
                'is_superuser':instance.user_id.is_superuser,
                'telephone':instance.user_id.telephone
            },
            'total':instance.total
        }


class DetalleTransaccionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DetalleTransaccion
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'transaction_id':{
                'id':instance.transaction_id.id,
                'transaction_type':instance.transaction_id.transaction_type,
                'transaction_date':instance.transaction_id.transaction_date,
                'user_id':{
                    'id':instance.transaction_id.user_id.id,
                    'first_name':instance.transaction_id.user_id.first_name,
                    'last_name':instance.transaction_id.user_id.last_name,
                    'email':instance.transaction_id.user_id.email,
                    'username':instance.transaction_id.user_id.email,
                    'is_superuser':instance.transaction_id.user_id.is_superuser,
                    'telephone':instance.transaction_id.user_id.telephone
                },
                'total':instance.transaction_id.total
            },
            'medicine_id':{
                'id':instance.medicine_id.id,
                'medicine_name':instance.medicine_id.medicine_name,
                'description':instance.medicine_id.description
            },
            'quantity':instance.quantity,
            'price':instance.price,
            'subtoral':instance.subtotal
        }
