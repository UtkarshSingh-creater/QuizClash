from rest_framework import serializers
from .models import QuizRoom

class QuizRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=QuizRoom
        fields='__all__'