from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CurrentUserListUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [
        TokenAuthentication,
    ]

    def get_object(self):
        return self.request.user
