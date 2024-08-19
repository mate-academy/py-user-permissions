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

list_create_actions = {
    "get": "list",
    "post": "create",
}

genres_list = GenreViewSet.as_view(
    actions=list_create_actions
)

cinema_hall_list = CinemaHallViewSet.as_view(
    actions=list_create_actions
)

actor_list = ActorViewSet.as_view(
    actions=list_create_actions
)

movie_list = MovieViewSet.as_view(
    actions=list_create_actions
)

movie_detail = MovieViewSet.as_view(
    actions={
        "get": "retrieve",
    }
)

order_list = OrderViewSet.as_view(
    actions=list_create_actions
)

router = routers.DefaultRouter()
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", genres_list, name="genre-list"),
    path("cinema_hall/", cinema_hall_list, name="cinemahall-list"),
    path("actors/", actor_list, name="actor-list"),
    path("movie/", movie_list, name="movie-list"),
    path("movie/<int:pk>/", movie_detail, name="movie-detail"),
    path("order/", order_list, name="order-list"),
]

app_name = "cinema"
