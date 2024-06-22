from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from user.views import UserRegisterView, UserLoginView, UserProfileView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="create"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("me/", UserProfileView.as_view(), name="manage")
]

app_name = "user"
