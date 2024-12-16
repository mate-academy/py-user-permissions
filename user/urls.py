from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from user.views import CreateUserView, ManageUserView


app_name = "user"

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path("login/", obtain_auth_token, name="login"),
]
