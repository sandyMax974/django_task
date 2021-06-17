from django.db import models
from rest_framework import serializers
from .models import Tile


class TileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tile
        fields = "__all__"
