from rest_framework import serializers
from .models import ProjectImage,Project
class ProjectImageSerializer(serializers.ModelSerializer):
  image = serializers.ImageField()
  class Meta:
    model = ProjectImage
    fields = ["id","name","image"]

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)
    project_cover = serializers.ImageField()
    stack = serializers.ListField(
        child=serializers.CharField(), allow_empty=True
    )

    class Meta:
        model = Project
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = ProjectImageSerializer(instance.images.all(), many=True).data
        return rep

    def to_internal_value(self, data):
        # Convert comma-separated string to list if needed
        if 'stack' in data and isinstance(data['stack'], str):
            data['stack'] = [item.strip() for item in data['stack'].split(',')]
        return super().to_internal_value(data)