from django.urls import path

from user.views import (
    CreateUserView,
    CreateTokenUser,
    ManageUserView,
)

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register"),
    path("login/", CreateTokenUser.as_view(), name="token"),
    path("me/", ManageUserView.as_view(), name="myself"),
]

app_name = "user"
