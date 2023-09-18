from rest_framework.response import Response
from rest_framework import generics

from ..models.question import Question
from ..serializers.question import QuestionSerializer


class RandomQuestion(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
