from django.urls import path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('about', views.AboutViewSet)
router.register('project', views.ProjectViewSet)



urlpatterns = router.urls