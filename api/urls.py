from django.urls import path,include
from rest_framework_nested import routers

from my_portfolio.views import ProjectImageViewSet,ProjectViewSet,BlogViewSet

router = routers.DefaultRouter()
router.register("project",ProjectViewSet)
router.register("blog,",BlogViewSet)
project_router = routers.NestedDefaultRouter(router, "project", lookup="project")
project_router.register("project_images", ProjectImageViewSet, basename="project-images")
# from core.views import  members
urlpatterns = [
    path('', include(router.urls)),
    path('', include(project_router.urls)),
]
