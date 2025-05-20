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
  
  queryset = ProjectImage.objects.all()
  serializer_class = ProjectImageSerializer

  def get_queryset(self):
    return ProjectImage.objects.filter(project_id=self.kwargs.get('project_pk'))

  def perform_create(self, serializer):
    serializer.save(project_id=self.kwargs.get('project_pk'))
