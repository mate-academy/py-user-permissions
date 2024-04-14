from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from user.views import (
    UserCreateView,
    UserLoginView,
    ManageUserView,
)

app_name = "user"

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="create"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage"),

]
