from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    authentication_classes = (TokenAuthentication, )
    # system will understand how to authenticate

    permission_classes = (IsAuthenticated, )
    # if you comment permission_classes the information will
    # be available without any protection

    def get_object(self):
        """
        Rewrite get_object in order to update only user that
        is currently authenticated. Prohibit user from changing
        password or other data of different from authenticated
        user
        """
        return self.request.user
