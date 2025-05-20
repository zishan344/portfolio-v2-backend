from django.shortcuts import render
from rest_framework import viewsets
from .models import ProjectImage,Project
from .serializers import ProjectImageSerializer,ProjectSerializer
from decouple import config
# Create your views here.



class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer

class ProjectImageViewSet(viewsets.ModelViewSet):
  # print(config("CLOUD_NAME"))
  queryset = ProjectImage.objects.all()
  serializer_class = ProjectImageSerializer
