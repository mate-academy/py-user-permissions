from django.urls import path

from .views import LoginUserView, CreateUserView, ManageUserView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='get-token'),
    path('me/', ManageUserView.as_view(), name='manage-user'),
]

app_name = 'user'
