from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Message(models.Model):
    sent_at = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=512)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name='recieved_messages', on_delete=models.CASCADE)
