from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreListCreateViewSet,
    ActorListCreateViewSet,
    CinemaHallListCreateViewSet,
    MovieListCreateViewSet,
    MovieRetrieveViewSet,
    MovieSessionViewSet,
    OrderListCreateViewSet,
)

genre_list = GenreListCreateViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})

actor_list = ActorListCreateViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})

cinemahall_list = CinemaHallListCreateViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})

movie_list = MovieListCreateViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})

movie_detail = MovieRetrieveViewSet.as_view(actions={
    "get": "retrieve",
})

order_list = OrderListCreateViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})

router = routers.DefaultRouter()
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", genre_list, name="genre-list"),
    path("actors/", actor_list, name="actor-list"),
    path("cinema_hall/", cinemahall_list, name="cinemahall-list"),
    path("movie/", movie_list, name="movie-list"),
    path("movie/<int:pk>", movie_detail, name="movie-detail"),
    path("orders/", order_list, name="order-list"),
]

app_name = "cinema"
