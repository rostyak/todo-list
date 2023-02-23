from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    readiness = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
