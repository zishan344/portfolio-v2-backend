from django.urls import path,include
from rest_framework import routers
from my_portfolio.views import ProjectImageViewSet,ProjectViewSet
router = routers.DefaultRouter()
router.register("project",ProjectViewSet)
# from core.views import  members
urlpatterns = [
    path('', include(router.urls)),
]
