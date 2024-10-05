from django.urls import path, include

from user.views import CreateUserView, LoginView, ManagerUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login", LoginView.as_view(), name="login"),
    path("me", ManagerUserView.as_view(), name="manage"),
]

app_name = "user"
