from django.urls import path

from user.views import UserCreateViews, CreateTokenViews, ManageUserViews

urlpatterns = [
    path("register/", UserCreateViews.as_view(), name="create"),
    path("login/", CreateTokenViews.as_view(), name="login"),
    path("me/", ManageUserViews.as_view(), name="manage"),
]

app_name = "user"
