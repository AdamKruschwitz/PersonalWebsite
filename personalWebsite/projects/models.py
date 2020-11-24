from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    github_link = models.CharField(max_length=128)
    project_finished = models.BooleanField(default=False)
