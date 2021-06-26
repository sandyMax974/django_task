from django.contrib import admin

# Register your models here.
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ("order", "title", "description", "type")

admin.site.register(Task, TaskAdmin)
