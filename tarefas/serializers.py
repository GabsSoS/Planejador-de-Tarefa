from rest_framework import serializers
from tarefas.models import Task

class TaskSerializaer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'