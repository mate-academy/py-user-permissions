from django.urls import path
from rest_framework.authtoken import views

from user.views import CreateTokenView, CreateUserView, ManageUserView

urlpatterns = [
    path("login/", CreateTokenView.as_view(), name="login"),
    path("register", CreateUserView.as_view(), name="create"),
    path("me", ManageUserView.as_view(), name="manage"),
]

app_name = "user"
