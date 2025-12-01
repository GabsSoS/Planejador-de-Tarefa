from rest_framework import generics
from planer.models import PersonalUser
from planer.serializer import PlanerSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser



class PlanerCreateListView(generics.ListCreateAPIView):
    queryset = PersonalUser.objects.all()
    serializer_class = PlanerSerializer

class PlanerRetriveUpdateDestroyerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonalUser.objects.all()
    serializer_class = PlanerSerializer