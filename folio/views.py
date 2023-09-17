from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import About, Project, ProjectImage
from .serializers import AboutSerializer, ProjectSerializer, ProjectImageSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view

class AboutViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectImageViewSet(ModelViewSet):
    serializer_class = ProjectImageSerializer

    def get_serializer_context(self):
        return {'project_id': self.kwargs['projects_pk']}

    def get_queryset(self):
        return ProjectImage.objects.filter(project_id=self.kwargs['projects_pk'])