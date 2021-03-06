from rest_framework import routers
from . import views
from django.urls import path, include


router = routers.DefaultRouter(trailing_slash=False)
router.register("tasks", viewset=views.TaskViewSet)

urlpatterns = [path("api/", include(router.urls))]
