from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):

    serializer_class = UserSerializer
