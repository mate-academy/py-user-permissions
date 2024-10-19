from django.urls import path, include
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
router.register("moviesessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("actors/", ActorViewSet.as_view(), name="actor-list"),
    path("genres/", GenreViewSet.as_view(), name="genre-list"),
    path("orders/", OrderViewSet.as_view({"get": "list"}), name="order-list"),
    path("cinema_halls/", CinemaHallViewSet.as_view(), name="cinemahall-list"),
    path("movies/", MovieViewSet.as_view({"get": "list"}), name="movie-list"),
    path("movies/<int:pk>/",
         MovieViewSet.as_view({"get": "retrieve"}),
         name="movie-detail"),
]

app_name = "cinema"
