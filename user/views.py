from rest_framework import generics

from .serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
