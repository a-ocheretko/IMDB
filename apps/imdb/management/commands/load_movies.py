import os.path
from django.core.management.base import BaseCommand, CommandError
from apps.imdb.models import Movie
import csv


class Command(BaseCommand):

    help = "Imports movies from tsv file"

    def add_arguments(self, parser):
        parser.add_argument("-f", "--file", type=str, required=True)

    def handle(self, *args, **options):
        file = options.get("file")

        if not os.path.exists(file):
            raise CommandError("File does not exist")

        with open(file, encoding="utf-8") as f:

            data = csv.DictReader(
                f,
                dialect=csv.excel_tab,
                fieldnames=[
                    "tconst",
                    "titleType",
                    "primaryTitle",
                    "originalTitle",
                    "isAdult",
                    "startYear",
                    'endYear',
                    'runtimeMinutes',
                    'genres'
                ],
            )

            for line in data:

                if (not line) or (not line['tconst'].startswith('tt')) or (not line['titleType'] in ['movie', 'short']):
                    continue

                movie_data = {
                    "title_type": line['titleType'],
                    "name": line['primaryTitle'],
                    "is_adult": line['isAdult'],
                    "year": None if line['startYear'] == "\\N" else int(line['startYear']),
                    "genres": None if line['genres'].startswith("\\N") else line['genres'].split(","),
                }

                movie, created = Movie.objects.get_or_create(imdb_id=line['tconst'], defaults=movie_data)

                if created:
                    Movie.objects.filter(id=movie.id).update(**movie_data)
