from django.shortcuts import render
from rest_framework import viewsets
from .models import ProjectImage
from .serializers import ProjectImageSerializer
from decouple import config
# Create your views here.

class ProjectImageViewSet(viewsets.ModelViewSet):
  # print(config("CLOUD_NAME"))
  queryset = ProjectImage.objects.all()
  serializer_class = ProjectImageSerializer
