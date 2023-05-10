from datetime import datetime

from django.db.models import F, Count
from rest_framework import viewsets, status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession, Order
from cinema.permissions import IsAdminOrIfAuthenticatedReadOnly

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
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_permissions(self):
        if self.action == "list" or self.action == "create":
            self.permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
        return super(GenreViewSet, self).get_permissions()


class ActorViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def list(self, request):
        queryset = Actor.objects.all()
        serializer = ActorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_permissions(self):
        if self.action == "list" or self.action == "create":
            self.permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
        return super(CinemaHallViewSet, self).get_permissions()


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_permissions(self):
        if self.action == (
                "list" or self.action == "create" or self.action == "retrieve"
        ):
            self.permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
        return super(MovieViewSet, self).get_permissions()

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
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

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

    def get_permissions(self):
        if self.action == (
                "list" or self.action == "retrieve"
                or self.action == "create" or self.action == "update"
                or self.action == "partial_update" or self.action == "destroy"
        ):
            self.permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
        return super(MovieSessionViewSet, self).get_permissions()


class OrderPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related(
        "tickets__movie_session__movie",
        "tickets__movie_session__cinema_hall"
    )
    serializer_class = OrderSerializer
    pagination_class = OrderPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return OrderListSerializer

        return OrderSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "create":
            self.permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
        return super(OrderViewSet, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
