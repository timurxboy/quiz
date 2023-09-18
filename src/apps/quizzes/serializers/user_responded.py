from rest_framework import serializers

from ..models.user_response import UserResponse


class UsersRespondedSerializer(serializers.ModelSerializer):
    user_name = serializers.StringRelatedField(source='user', read_only=True)

    class Meta:
        model = UserResponse
        fields = ['user_name']
