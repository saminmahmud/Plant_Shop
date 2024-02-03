from django.shortcuts import render
from rest_framework import viewsets
from .models import Plant
from .serializers import PlantSerializer

class PlantViewset(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
