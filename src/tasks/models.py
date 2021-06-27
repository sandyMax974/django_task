from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=30, default="none")
    order = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True, default="none")
    type = models.CharField(max_length=30, default="none")
    tile = models.ForeignKey(
        "tiles.Tile", on_delete=models.CASCADE, blank=True, null=True
    )

    def _str_(self):
        return self.title