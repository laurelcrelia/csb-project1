from django.db import models

class Timer(models.Model):
    title = models.CharField(max_length=100)
    expiration_date = models.DateTimeField()
