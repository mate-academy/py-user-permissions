from django.urls import path
from .views import CreateUserView, UserLoginView, UserMeView

app_name = "user"

urlpatterns = [
    path("create/", CreateUserView.as_view(), name="create"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("me/", UserMeView.as_view(), name="manage"),
]
