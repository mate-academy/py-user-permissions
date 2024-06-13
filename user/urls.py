from django.urls import path, include

from user.views import CreateUserAPIView

urlpatterns = [
    path("register/", CreateUserAPIView.as_view(), name="create"),
]


app_name = "user"
