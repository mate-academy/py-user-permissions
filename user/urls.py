from django.urls import path

from user.views import RegisterUserView, LoginTokenView, UserProfileView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="create"),
    path("login/", LoginTokenView.as_view(), name="login"),
    path("me/", UserProfileView.as_view(), name="manage"),
]

app_name = "user"
