from django.urls import path

from user.views import CreateUserView, LoginUserView, MangerUserView


urlpatterns = [
    path("create/", CreateUserView.as_view(), name="create"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("me/", MangerUserView.as_view(), name="manage"),
]

app_name = "user"
