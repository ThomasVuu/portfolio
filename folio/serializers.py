from django.db import models
from rest_framework import serializers
from .models import About, Project, ProjectImage

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['hello', 'about_text', 'about_image']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'start_year', 'description', 'url', 'github']

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['image']
