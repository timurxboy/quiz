from rest_framework import serializers
from ..models.user_response import UserResponse


class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResponse
        fields = ['question', 'answer']
        read_only_fields = ('user', 'is_correct')
