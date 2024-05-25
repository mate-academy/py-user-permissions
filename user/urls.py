from django.urls import path

from user import views

urlpatterns = [
    path("register/", views.UserRegistrationView.as_view(), name="create"),
    path("login/", views.UserLoginSerializer.as_view(), name="login"),
    path("me/", views.UserManagementView.as_view(), name="manage"),

]

app_name = "user"
