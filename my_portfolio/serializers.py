from rest_framework import serializers
from .models import ProjectImage,Project,Blog
class ProjectImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = ProjectImage
        fields = "__all__"

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

class BlogSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Blog
        fields = "__all__"