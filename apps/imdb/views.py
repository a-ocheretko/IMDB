from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *


class AbstractListCreateAPIView(ListCreateAPIView):
    serializer_class = None
    model = None

    def get_queryset(self):
        return self.model.objects.all()


class AbstractRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = None
    model = None

    def get_queryset(self):
        return self.model.objects.all()


class MovieListCreateAPIView(AbstractListCreateAPIView):
    serializer_class = MovieSerializer
    model = Movie


class MovieRetrieveUpdateDestroyAPIView(AbstractRetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    model = Movie


class PersonListCreateAPIView(AbstractListCreateAPIView):
    serializer_class = PersonSerializer
    model = Person


class PersonRetrieveUpdateDestroyAPIView(AbstractRetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    model = Person


class PersonMovieListCreateAPIView(AbstractListCreateAPIView):
    serializer_class = PersonMovieSerializerMin
    model = PersonMovie


class PersonMovieRetrieveUpdateDestroyAPIView(AbstractRetrieveUpdateDestroyAPIView):
    serializer_class = PersonMovieSerializer
    model = PersonMovie
