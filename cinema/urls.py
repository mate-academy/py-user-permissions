from django.urls import path, include
from rest_framework import routers
# from django.urls import reverse

from cinema import views
from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    OrderViewSet,
)
# url = reverse('create')
router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("order", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path('create/', views.create_view, name='create')
]

app_name = "cinema"
