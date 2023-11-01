from django.urls import path, include
from user.views import CreateUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register")
]

app_name = "user"
