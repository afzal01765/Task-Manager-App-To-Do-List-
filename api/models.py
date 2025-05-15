from django.db import models
from django.contrib.auth.models import User
import datetime

class Category(models.Model):
    title = models.CharField(max_length=128, unique=True)

    def __str__(self) -> str:
        return self.title


class TodoTask(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    due_date = models.DateTimeField(default=datetime.datetime.now())
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    tags = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.title