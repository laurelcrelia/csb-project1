from django.db import models
from django.contrib.auth.models import User

class Timer(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    expiration_date = models.DateTimeField()
