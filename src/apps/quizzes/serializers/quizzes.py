from rest_framework import serializers
from ..models.quiz import Quizzes


class QuizzesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]







