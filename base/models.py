from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)
    discription = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    saved = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

