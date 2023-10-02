from django.db import models
from django.utils import timezone

class Message(models.Model):
    sent_at = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=512)
