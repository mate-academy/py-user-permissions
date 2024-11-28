from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path("register/", views.CreateUserView.as_view(), name="user-register"),
    path("login/", views.LoginUserView.as_view(), name="user-login"),
    path("me/", views.ManageUserView.as_view(), name="user-update")
]
