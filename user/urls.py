from django.urls import path

from user.views import CreateUserViews, CreateTokenViews, ManageUserViews

urlpatterns = [
    path("register/", CreateUserViews.as_view(), name="create"),
    path("login/", CreateTokenViews.as_view(), name="login"),
    path("me/", ManageUserViews.as_view(), name="manage"),
]

app_name = "user"
