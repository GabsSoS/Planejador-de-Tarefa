from rest_framework import serializers
from task.models import Task
from django.contrib.auth.models import User
from rest_framework import serializers

class TaskSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'create_date',
            'end_date', 'description', 'task_status', 'owner'
            ]
    

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()