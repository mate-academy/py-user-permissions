from django.urls import path

from user.views import UserCreateView, LoginUserView, UserRetrieveUpdateView

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="create"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("me/", UserRetrieveUpdateView.as_view(), name="manage"),
]

app_name = "user"
