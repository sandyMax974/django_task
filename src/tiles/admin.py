from django.contrib import admin

# Register your models here.
from .models import Tile


class TileAdmin(admin.ModelAdmin):
    list_display = ("launchDate", "status")


admin.site.register(Tile, TileAdmin)
