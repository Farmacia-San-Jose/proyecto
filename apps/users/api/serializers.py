from rest_framework import serializers
from apps.users.models import User

#from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','username','password','telephone','is_superuser']
        
            