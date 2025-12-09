from rest_framework import generics
from task.serializers import TaskSerializers, UserRegisterSerializer
from django.contrib.auth.models import User
from task.models import Task
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

class TaskRetriveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers



