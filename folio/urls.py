from django.urls import path
from . import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('about', views.AboutViewSet)
router.register('projects', views.ProjectViewSet)

projects_router = routers.NestedDefaultRouter(router, 'projects', lookup='projects')
projects_router.register('images', views.ProjectImageViewSet, basename='project-images')



urlpatterns = router.urls + projects_router.urls