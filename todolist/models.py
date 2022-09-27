from django.db import models 
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    title = models.TextField()
    description = models.TextField()
