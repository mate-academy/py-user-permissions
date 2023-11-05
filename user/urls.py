from django.urls import path

from user.views import UserCreateView

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="create"),
]

app_name = "user"
