from django.urls import path
from user.views import CreateUserView, CreateTokenView, ManageUserView

urlpatterns = [
    path("user/register/", CreateUserView.as_view(), name="register"),
    path("user/login/", CreateTokenView.as_view(), name="token"),
    path("user/me/", ManageUserView.as_view(), name="manage"),
]
