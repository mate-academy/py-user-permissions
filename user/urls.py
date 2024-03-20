from django.urls import path
from rest_framework.authtoken import views

from .views import (
    CreateUserView,
    LoginUserView,
    ManageUserView
)

urlpatterns = [
    path(
        "register/",
        CreateUserView.as_view(),
        name="create_user"
    ),
    path(
        "login/",
        LoginUserView.as_view(),
        name="get_auth_token"
    ),
    path(
        "me/",
        ManageUserView.as_view(),
        name="manage_user"
    )
]

app_name = "user"
