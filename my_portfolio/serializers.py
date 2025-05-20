from rest_framework import serializers
from .models import ProjectImage,Project
class ProjectImageSerializer(serializers.ModelSerializer):
  image = serializers.ImageField()
  class Meta:
    model = ProjectImage
    fields = ["id","image"]

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)
    project_cover = serializers.ImageField()
    stack = serializers.ListField(child=serializers.CharField(max_length=50), required=False)

    class Meta:
        model = Project
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = ProjectImageSerializer(instance.images.all(), many=True).data
        return rep