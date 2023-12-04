from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "password", "email", "is_staff")
        read_only_fields = ("id", "is_staff")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data["password"]

        if len(password) < 5:
            raise serializers.ValidationError(
                {"password": ["Length of password must be > than 5!"]}
            )

        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password")
        user = super().update(instance, validated_data)

        if password:

            if len(password) < 5:
                raise serializers.ValidationError(
                    {"password": ["Length of password must be > than 5!"]}
                )

            user.set_password(password)
            user.save()

        return user
