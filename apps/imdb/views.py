from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *


class BaseListCreateAPIView(ListCreateAPIView):
    serializer_class = None
    model = None

    def get_queryset(self):
        return self.model.objects.all()


class BaseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = None
    model = None

    def get_queryset(self):
        return self.model.objects.all()


class MovieListCreateAPIView(BaseListCreateAPIView):
    serializer_class = DirectorMovieSerializer
    model = Movie


class MovieRetrieveUpdateDestroyAPIView(BaseRetrieveUpdateDestroyAPIView):
    serializer_class = DirectorMovieSerializer
    model = Movie


class PersonListCreateAPIView(BaseListCreateAPIView):
    serializer_class = PersonSerializer
    model = Person


class PersonRetrieveUpdateDestroyAPIView(BaseRetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    model = Person


class PersonMovieListCreateAPIView(BaseListCreateAPIView):
    serializer_class = PersonMovieSerializerMin
    model = PersonMovie


class PersonMovieRetrieveUpdateDestroyAPIView(BaseRetrieveUpdateDestroyAPIView):
    serializer_class = PersonMovieSerializer
    model = PersonMovie
