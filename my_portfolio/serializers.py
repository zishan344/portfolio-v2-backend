from rest_framework import serializers
from .models import ProjectImage
class ProjectImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectImage
    fields = ["id","name","image"]
