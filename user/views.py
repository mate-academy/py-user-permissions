from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from user.serializers import UserSerializers


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializers


class CreateTokenView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        return self.request.user
