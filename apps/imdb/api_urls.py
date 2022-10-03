import os
from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

app_name = 'apps.imdb'

urlpatterns = [
    path('movie/',
         (MovieListCreateAPIView.as_view()),
         name='movie-list-create'),
    path('movie/<str:pk>/',
         cache_page(int(os.getenv('IMDB_CACHE_TIMEOUT')))(MovieRetrieveUpdateDestroyAPIView.as_view()),
         name='movie-list-retrieve-update-destroy'),
    path('person/',
         cache_page(int(os.getenv('IMDB_CACHE_TIMEOUT')))(PersonListCreateAPIView.as_view()),
         name='person-list-create'),
    path('person/<str:pk>/',
         cache_page(int(os.getenv('IMDB_CACHE_TIMEOUT')))(PersonRetrieveUpdateDestroyAPIView.as_view()),
         name='person-list-retrieve-update-destroy'),
    path('personmovie/',
         cache_page(int(os.getenv('IMDB_CACHE_TIMEOUT')))(PersonMovieListCreateAPIView.as_view()),
         name='personmovie-list-create'),
    path('personmovie/<str:pk>/',
         cache_page(int(os.getenv('IMDB_CACHE_TIMEOUT')))(PersonMovieRetrieveUpdateDestroyAPIView.as_view()),
         name='personmovie-list-retrieve-update-destroy'),
]
