# tweet/serializers.py
from rest_framework import serializers
from .models import Twiit

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Twiit
        fields = ['id', 'text', 'created_at']
