from rest_framework import routers
from . import views
from django.urls import path, include


router = routers.DefaultRouter()
router.register("tiles", viewset=views.TileViewSet)

urlpatterns = [path("", include(router.urls))]
