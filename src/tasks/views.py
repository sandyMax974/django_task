from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializer import TaskSerializer

# from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("order")
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all().order_by("order")

        param = self.request.query_params.get("tile_id", None)
        if param:
            queryset = queryset.filter(tile_id=param)

        return queryset
