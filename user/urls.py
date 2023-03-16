from django.urls import path

from cinema.views import CreateUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register")
]

app_name = "user"
