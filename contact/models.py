from django.utils import timezone

from django.db import models


# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=200, default='')
    subject = models.CharField(max_length=200, default='')
    message = models.CharField(max_length=1000, default='')
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email


    class Meta:
        ordering = ['-datetime']