from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from user.serializers import UserCreateUpdateSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserCreateUpdateSerializer

    def get_object(self):
        return self.request.user


class UserDetailUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserCreateUpdateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserAuthentication(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
