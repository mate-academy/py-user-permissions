from django.urls import path

from user.views import (
    CreateUserView,
    CreateTokenView,
    ManageUser
)

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="token"),
    path("me/", ManageUser.as_view(), name="manage")
]

app_name = "user"
