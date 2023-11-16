from rest_framework import serializers
from .models import Message


class MessgageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message