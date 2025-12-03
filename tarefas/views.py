
from django.contrib.auth import authenticate, login
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tarefas.models import Task
from tarefas.serializers.SRTask import TaskSerializaer
from tarefas.serializers.SRUser import RegisterSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuário registrado com sucesso"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
class LoginView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # cria sessão
            return Response({"message": "Login realizado com sucesso"}, status=status.HTTP_200_OK)
        return Response({"error": "Credenciais inválidas"}, status=status.HTTP_400_BAD_REQUEST)



class TaskCreateListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializaer
    