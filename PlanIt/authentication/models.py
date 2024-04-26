
from django.db import models

class Task(models.Model):
    status = models.BooleanField(default=True)
    task_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
