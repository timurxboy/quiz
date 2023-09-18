from django.db import models
from django.contrib.auth.models import User
from..models.question import Question
from ..models.answer import Answer


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='user_response')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='user_response')
    is_correct = models.BooleanField(default=False)