from django.urls import path

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    OrderViewSet,
)


urlpatterns = [
    path(
        "genres/",
        GenreViewSet.as_view({"get": "list", "post": "create"}),
        name="genre-list"
    ),
    path(
        "actors/",
        ActorViewSet.as_view({"get": "list", "post": "create"}),
        name="actor-list"
    ),
    path(
        "cinema_halls/",
        CinemaHallViewSet.as_view({"get": "list", "post": "create"}),
        name="cinemahall-list"
    ),
    path(
        "orders/",
        OrderViewSet.as_view({"get": "list", "post": "create"}),
        name="order-list"
    ),
    path(
        "movies/",
        MovieViewSet.as_view({"get": "list", "post": "create"}),
        name="movie-list"
    ),
    path(
        "movies/<int:pk>/",
        MovieViewSet.as_view({"get": "retrieve"}),
        name="movie-detail"
    ),
    path(
        "moviesessions/",
        MovieSessionViewSet.as_view(
            {
                "get": "list",
                "post": "create"
            }
        ),
        name="moviesession-list"
    ),
    path(
        "moviesessions/<int:pk>/",
        MovieSessionViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy"
            }
        ),
        name="moviesession-detail"),
]

app_name = "cinema"
