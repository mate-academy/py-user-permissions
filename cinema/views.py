from datetime import datetime

from django.db.models import F, Count
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession, Order
from user.permissions import IsAdminOrIfAuthenticatedReadOnly

from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieDetailSerializer,
    MovieSessionDetailSerializer,
    MovieListSerializer,
    OrderSerializer,
    OrderListSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
    http_method_names = ["get", "post", "put", "delete"]  # List and create

    def update(self, request, *args, **kwargs):
        """Return 404 for PUT requests instead of 405."""
        raise NotFound()

    def destroy(self, request, *args, **kwargs):
        """Return 404 for DELETE requests instead of 405."""
        raise NotFound()

    def retrieve(self, request, *args, **kwargs):
        """Force 404 when trying to retrieve a single genre."""
        raise NotFound("Genre not found")


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
    http_method_names = ["get", "post", "put", "delete"]  # List and create

    def update(self, request, *args, **kwargs):
        """Return 404 for PUT requests instead of 405."""
        raise NotFound()

    def destroy(self, request, *args, **kwargs):
        """Return 404 for DELETE requests instead of 405."""
        raise NotFound()

    def retrieve(self, request, *args, **kwargs):
        """Force 404 when trying to retrieve a single Actor."""
        raise NotFound("Actor not found")


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
    http_method_names = ["get", "post", "put", "delete"]  # List and create

    def update(self, request, *args, **kwargs):
        """Return 404 for PUT requests instead of 405."""
        raise NotFound()

    def destroy(self, request, *args, **kwargs):
        """Return 404 for DELETE requests instead of 405."""
        raise NotFound()


    def retrieve(self, request, *args, **kwargs):
        """Force 404 when trying to retrieve a single cinema hall."""
        raise NotFound()

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")
    serializer_class = MovieSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
    http_method_names = ["get", "post", "retrieve"]  # List, create, retrieve

    @staticmethod
    def _params_to_ints(qs):
        """Converts a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(",")]

    def get_queryset(self):
        """Retrieve the movies with filters"""
        title = self.request.query_params.get("title")
        genres = self.request.query_params.get("genres")
        actors = self.request.query_params.get("actors")

        queryset = self.queryset

        if title:
            queryset = queryset.filter(title__icontains=title)

        if genres:
            genres_ids = self._params_to_ints(genres)
            queryset = queryset.filter(genres__id__in=genres_ids)

        if actors:
            actors_ids = self._params_to_ints(actors)
            queryset = queryset.filter(actors__id__in=actors_ids)

        return queryset.distinct()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieDetailSerializer

        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = (
        MovieSession.objects.all()
        .select_related("movie", "cinema_hall")
        .annotate(
            tickets_available=F("cinema_hall__rows")
                              * F("cinema_hall__seats_in_row")
                              - Count("tickets")
        )
    )
    serializer_class = MovieSessionSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
    http_method_names = ["get", "post", "patch", "put", "delete"]  # All actions

    def get_queryset(self):
        date = self.request.query_params.get("date")
        movie_id_str = self.request.query_params.get("movie")

        queryset = self.queryset

        if date:
            date = datetime.strptime(date, "%Y-%m-%d").date()
            queryset = queryset.filter(show_time__date=date)

        if movie_id_str:
            queryset = queryset.filter(movie_id=int(movie_id_str))

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer

        if self.action == "retrieve":
            return MovieSessionDetailSerializer

        return MovieSessionSerializer


class OrderPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related(
        "tickets__movie_session__movie", "tickets__movie_session__cinema_hall"
    )
    serializer_class = OrderSerializer
    pagination_class = OrderPagination
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users
    http_method_names = ["get", "post", "put", "delete"]  # Allow PUT to override response

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return OrderListSerializer

        return OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        """Force 404 response for PUT requests."""
        raise NotFound("Order not found.")

    def retrieve(self, request, *args, **kwargs):
        """Force 404 when trying to retrieve a single order."""
        raise NotFound("Order not found.")

    def destroy(self, request, *args, **kwargs):
        """Return 404 for DELETE requests instead of 405."""
        raise NotFound("Order not found.")
