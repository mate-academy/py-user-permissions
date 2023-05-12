from django.urls import path
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    OrderViewSet,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("genres/", GenreViewSet.as_view(), name="genre-list"),
    path("cinema_halls/", CinemaHallViewSet.as_view(), name="cinemahall-list"),
    path("actors/", ActorViewSet.as_view(), name="actor-list"),
    path("orders/", OrderViewSet.as_view(), name="order-list")
] + router.urls

app_name = "cinema"
