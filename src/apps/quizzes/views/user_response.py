from rest_framework import generics, status
from rest_framework.response import Response

from ..models.answer import Answer
from ..serializers.user_response import UserResponseSerializer
from rest_framework import permissions
from ..models.user_response import UserResponse


class UserResponseView(generics.CreateAPIView):
    queryset = UserResponse
    serializer_class = UserResponseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        question = serializer.validated_data.get('question')
        answer = serializer.validated_data.get('answer')
        user_response = UserResponse.objects.filter(user=user, question=question)

        if user_response.exists():
            return Response(
                {"detail": "You have already answered this question"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if str(Answer.objects.get(id=answer.id).question.title) == str(question):

            if Answer.objects.get(id=answer.id).is_right:
                UserResponse.objects.create(user=user, question=question, answer=answer, is_correct=True)
                return Response(
                    {'detail': 'You answered round !'},
                    status=status.HTTP_201_CREATED
                )

            UserResponse.objects.create(user=user, question=question, answer=answer)
            return Response(
                {'detail': 'You answered unequivocally !'},
                status=status.HTTP_201_CREATED
            )

        return Response(
            {'detail': 'Not the answer to the question !'},
            status=status.HTTP_400_BAD_REQUEST
        )
