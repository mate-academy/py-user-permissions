from django.urls import path
from rest_framework.authtoken import views

from user.views import CreateUserView, CreateToken, ManageUserView


urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register"),
    path("login/", CreateToken.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage"),
]

app_name = "user"
