from rest_framework import generics
from rest_framework.response import Response

from src.apps.quizzes.models.quiz import Quizzes
from src.apps.quizzes.models.user_response import UserResponse
from src.apps.quizzes.serializers.response_all_results import QuizSerializer


class ResponseAllResultsView(generics.ListAPIView):
    serializer_class = QuizSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        user_responses = UserResponse.objects.filter(user=user)
        quizzes = Quizzes.objects.filter(questions__user_response__in=user_responses).distinct()
        serializer = QuizSerializer(quizzes, many=True, context={'request': request}).data
        return Response(serializer)
