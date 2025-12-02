from rest_framework import generics
from tarefas.models import Task
from tarefas.serializers import TaskSerializaer
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt


import json

@csrf_exempt
def registrar_usuario(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Usuário já existe"}, status=400)

        user = User.objects.create_user(username=username, password=password, email=email)
        return JsonResponse({"message": "Usuário criado com sucesso", "id": user.id})
    return JsonResponse({"error": "Método não permitido"}, status=405)

@csrf_exempt
def login_usuario(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login realizado com sucesso"})
        else:
            return JsonResponse({"error": "Credenciais inválidas"}, status=400)
    return JsonResponse({"error": "Método não permitido"}, status=405)


class TaskCreateListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializaer
    