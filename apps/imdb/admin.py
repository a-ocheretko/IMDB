from django.contrib import admin
from .models import *


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('title_type', 'is_adult')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(PersonMovie)
class PersonMovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'movie')
