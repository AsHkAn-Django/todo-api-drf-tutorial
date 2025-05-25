from django.db import models
from django.conf import settings



class Task(models.Model):
    title = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="tasks", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title