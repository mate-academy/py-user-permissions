from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email", "password", "is_staff")
        read_only_fie = ("id", "is_staff")
        extra_kwargs = {"password": {"write_only": True}, "min_lenght": 5}

        def create(self, validation_data):
            return get_user_model().object.create_user(**validation_data)

