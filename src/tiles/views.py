from django.shortcuts import render
from rest_framework import viewsets
from .models import Tile
from .serializer import TileSerializer

# Create your views here.


class TileViewSet(viewsets.ModelViewSet):
    queryset = Tile.objects.all().order_by("launchDate")
    serializer_class = TileSerializer
