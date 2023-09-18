from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.question import Question
from ..serializers.question import QuestionSerializer


class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)
