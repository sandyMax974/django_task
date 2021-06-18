from rest_framework import routers
from . import views
from django.urls import path, include


router = routers.DefaultRouter(trailing_slash=False)
router.register("tiles", viewset=views.TileViewSet)

urlpatterns = [path("api/", include(router.urls))]
