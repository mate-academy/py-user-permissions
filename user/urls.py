from django.urls import path

from user.views import (
    UserCreationView,
    UserLoginView,
    ManageUserView
)

urlpatterns = [
    path("register/", UserCreationView.as_view(), name="create"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage")
]

app_name = "user"
