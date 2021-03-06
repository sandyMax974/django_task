from django.db import models
from django.contrib import admin

# Create your models here.
class Tile(models.Model):
    launchDate = models.DateField(auto_now=False, auto_now_add=False)
    STATUSES = (("live", "LIVE"), ("pending", "PENDING"), ("archive", "ARCHIVE"))
    status = models.CharField(max_length=7, choices=STATUSES)

    def _str_(self):
        return self.launchDate
