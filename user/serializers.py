from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "email",
            "is_staff",
            "password",
        )
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}
        read_only_fields = ("id", "is_staff")

    def create(self, validated_data):
        user = get_user_model()
        return user.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password")
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
