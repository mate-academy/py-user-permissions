from django.urls import path

from user.views import (
    UserRegisterView,
    UserRetrieveUpdateView,
    UserLoginView
)


urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="create"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("me/", UserRetrieveUpdateView.as_view(), name="manage"),
]


app_name = "user"
