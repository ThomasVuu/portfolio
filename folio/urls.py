from django.urls import path
from . import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('about', views.AboutViewSet)
router.register('projects', views.ProjectViewSet)
router.register('experience', views.ExperienceViewSet)

projects_router = routers.NestedDefaultRouter(router, 'projects', lookup='projects')
projects_router.register('images', views.ProjectImageViewSet, basename='project-images')

experience_router = routers.NestedDefaultRouter(router, 'experience', lookup='experience')
experience_router.register('technologies', views.ExperienceTechnologyViewSet, basename='experience-technologies')



urlpatterns = router.urls + projects_router.urls + experience_router.urls