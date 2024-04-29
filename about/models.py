from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Admin(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"