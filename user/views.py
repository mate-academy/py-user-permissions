from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.settings import api_settings

from user.serializers import UserSerializer


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserLoginView(ObtainAuthToken):
    permission_classes = (AllowAny,)
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
