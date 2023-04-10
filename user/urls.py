from django.urls import path
from rest_framework.authtoken import views

from user.views import (
    CreateUserView,
    CreateTokenView
)

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="token")
]

app_name = "user"
