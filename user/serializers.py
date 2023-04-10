from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "password", "is_staff"]
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 5}
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        password = validated_data.get("password")
        if password:
            instance.set_password(password)
        instance.email = validated_data.get("email", instance.email)
        instance.is_staff = validated_data.get("is_staff", instance.is_staff)
        instance.save()
        return instance
