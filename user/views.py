from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


