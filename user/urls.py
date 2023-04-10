from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.CreateUserView.as_view(), name="create"),
    path("login/", views.CreateTokenView.as_view(), name="login"),
    path("me/", views.ManageUserView.as_view(), name="manage"),
]

app_name = "user"
