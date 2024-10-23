from rest_framework import viewsets
from cinema.serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from user.permissions import IsAdminOrIfAuthenticatedReadOnly
from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession, Order


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()
    permission_classes = [IsAuthenticated]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
