from django.urls import path

from user.views import CreateUserView

urlpatterns = [
	path("register/", CreateUserView.as_view(), name="create"),
	# path("login/"),
	# path("me/"),
]

app_name = "user"
