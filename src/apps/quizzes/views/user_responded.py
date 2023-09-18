from rest_framework import generics, permissions
from rest_framework.response import Response

from src.apps.quizzes.models.user_response import UserResponse
from ..serializers.user_responded import UsersRespondedSerializer


class UsersRespondedView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        answer = UserResponse.objects.filter(answer__answer_text=kwargs['answer'])
        serializer = UsersRespondedSerializer(answer, many=True)
        print(serializer.data)
        return Response(serializer.data)
