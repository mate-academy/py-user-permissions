from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/cinema/", include("cinema.urls", namespace="cinema")),
    path("api/user/", include('user.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
