from rest_framework import serializers
from planer.models import PersonalUser

class PlanerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PersonalUser
        fields = '__all__'