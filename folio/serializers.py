from django.db import models
from rest_framework import serializers
from .models import About, Project, ProjectImage

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['hello', 'about_text', 'about_image']

class ProjectImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        project_id = self.context.get('project_id')
        return ProjectImage.objects.create(project_id=project_id, **validated_data)
    class Meta:
        model = ProjectImage
        fields = ['id','image']

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['title', 'start_year', 'description', 'url', 'github', 'images']

