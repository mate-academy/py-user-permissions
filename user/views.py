from rest_framework import generics

from user.models import User
from user.serializers import UserSerializer


class CreateUserView(generics.GenericAPIView):
    serializer_class = UserSerializer
