from django.shortcuts import render
from rest_framework import viewsets
from .models import ProjectImage,Project
from .serializers import ProjectImageSerializer,ProjectSerializer
from decouple import config
from rest_framework.permissions import BasePermission, SAFE_METHODS
# Create your views here.

class IsAdminOrReadOnly(BasePermission):
  """
  Custom permission to only allow admins to edit objects.
  """
  def has_permission(self, request, view):
    # Allow read-only access for all users
    if request.method in SAFE_METHODS:
      return True
    # Allow write access only for admin users
    return request.user and request.user.is_staff


class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  permission_classes = [IsAdminOrReadOnly]
  

class ProjectImageViewSet(viewsets.ModelViewSet):
  
  queryset = ProjectImage.objects.all()
  serializer_class = ProjectImageSerializer
  permission_classes = [IsAdminOrReadOnly]

  def get_queryset(self):
    return ProjectImage.objects.filter(project_id=self.kwargs.get('project_pk'))

  def perform_create(self, serializer):
    serializer.save(project_id=self.kwargs.get('project_pk'))
