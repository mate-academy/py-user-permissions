from rest_framework import generics

from user.serializers import UserCreateSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
