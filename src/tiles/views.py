from django.shortcuts import render
from rest_framework import viewsets
from .models import Tile
from .serializer import TileSerializer

# Create your views here.


class TileViewSet(viewsets.ModelViewSet):
    queryset = Tile.objects.all().order_by("launchDate")
    serializer_class = TileSerializer

    def get_queryset(self):
        queryset = Tile.objects.all().order_by("launchDate")

        param = self.request.query_params.get("status", None)
        if param:
            queryset = queryset.filter(status=param)

        return queryset
