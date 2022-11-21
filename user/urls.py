from django.urls import path

from user.views import CreateUserAPI, CreateTokenView, ManageAPIView

urlpatterns = [
    path("register/", CreateUserAPI.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="login"),
    path("me/", ManageAPIView.as_view(), name="manage"),
]

app_name = "user"
