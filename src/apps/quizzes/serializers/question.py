from rest_framework import serializers

from ..models.question import Question
from ..serializers.answer import AnswerSerializer


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'answers']
