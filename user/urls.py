from django.urls import path

from user.views import UserLoginView, UserRegistrationView, UserDetailView


app_name = "user"

urlpatterns = [
    path("me/", UserDetailView.as_view(), name="manage"),
    path("register/", UserRegistrationView.as_view(), name="create"),
    path("login/", UserLoginView.as_view(), name="login"),
]
