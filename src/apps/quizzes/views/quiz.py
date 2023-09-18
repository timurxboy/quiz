from rest_framework import generics
from ..models.quiz import Quizzes
from ..serializers.quizzes import QuizzesSerializer


class Quiz(generics.ListAPIView):
    serializer_class = QuizzesSerializer
    queryset = Quizzes.objects.all()

