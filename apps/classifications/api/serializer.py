# API
from rest_framework import serializers

# MODELS
from apps.classifications.models import UsoTerapeutico, FormaAdministracion, Clasificacion

# SERIALIZER
from apps.medicines.api.serializer import MedicamentoSerializer

class UsoTerapeuticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsoTerapeutico
        fields = '__all__'

class FormaAdministracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaAdministracion
        fields = '__all__'

class ClasificacionSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Clasificacion
        fields = '__all__'
    ''' 
    def to_representation(self, instance):
        return {
            'medicine_id':{
                'id':instance.medicine_id.id,
                'medicine_name':instance.medicine_id.id,
                'description':instance.medicine_id.description
            },
            'therepeuticuse_id':{
                'id':instance.therepeuticuse_id.id,
                'type_therepeuticuse':instance.therepeuticuse_id.type_therepeuticuse,
                'description':instance.therepeuticuse_id.description,
                
            },
            'formadministration_id':{
                'id':instance.formadministration_id.id,
                'type_administrationform':instance.formadministration_id.type_adminstrationform,
                'description':instance.formadministration_id.description
            },
        }
        '''