from django.urls import path

from user.views import CreateUserView, LoginUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", LoginUserView.as_view(), name="token"),
]

app_name = "user"
