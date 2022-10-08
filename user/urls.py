from django.urls import path
from rest_framework.authtoken import views

from user.views import CreateUserView, UserAuthentication, UserDetailUpdateView

urlpatterns = [
    path("login/", UserAuthentication.as_view(), name="login"),
    path("register/", CreateUserView.as_view(), name="create"),
    path("me/", UserDetailUpdateView.as_view(), name="manage"),
]


app_name = "user"
