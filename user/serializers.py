from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.db import transaction


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email", "password", "is_staff")
        read_only_fields = ("id", "is_staff")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = get_user_model().objects.select_for_update().get(pk=instance.pk)
        for attr, value in validated_data.items():
            setattr(user, attr, value)
        user.save()

        if password:
            user.set_password(password)
            user.save()

        return user
