from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Movie(models.Model):

    class TitleType(models.TextChoices):
        SHORT = 'short', _('Short')
        MOVIE = 'movie', _('Movie')

    imdb_id = models.CharField(max_length=255, verbose_name=_("IMDB ID"))
    title_type = models.CharField(max_length=255, choices=TitleType.choices, verbose_name=_("Title Type"))
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    is_adult = models.BooleanField(verbose_name=_('Adult'))
    year = models.IntegerField(verbose_name=_("Release Year"), null=True)
    genres = ArrayField(models.CharField(max_length=255), verbose_name=_("Genres"), null=True)

    def __str__(self):
        return self.name


class Person(models.Model):

    imdb_id = models.CharField(max_length=255, verbose_name=_("IMDB ID"))
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    birth_year = models.IntegerField(verbose_name=_("Birth Year"), null=True)
    death_year = models.IntegerField(verbose_name=_("Death Year"), null=True)

    def __str__(self):
        return self.name


class PersonMovie(models.Model):

    movie = models.ForeignKey(to=Movie, on_delete=models.PROTECT, verbose_name=_("Movie"))
    person = models.ForeignKey(to=Person, on_delete=models.PROTECT, verbose_name=_("Person"))
    ordering = models.IntegerField(verbose_name=_("Ordering"))
    category = models.CharField(max_length=255, verbose_name=_("Category"))
    job = models.CharField(max_length=255, verbose_name=_("Job"), null=True)
    characters = ArrayField(models.CharField(max_length=255), verbose_name=_("Characters"), null=True)

    def __str__(self):
        return str(self.person) if self.category == 'director' else ''
