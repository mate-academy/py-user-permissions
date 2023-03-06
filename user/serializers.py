from django.contrib.auth import get_user_model
from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email", "is_staff")
        read_only = ("id", "is_staff")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data: dict) -> User:
        """Create user with encrypted password"""
        return get_user_model().create_user(**validated_data)
