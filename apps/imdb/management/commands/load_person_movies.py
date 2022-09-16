import json
import os.path
from django.core.management.base import BaseCommand, CommandError
from apps.imdb.models import Movie, Person, PersonMovie
import csv


class Command(BaseCommand):

    help = "Imports person+movies from tsv file"

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
                    "ordering",
                    "nconst",
                    "category",
                    "job",
                    "characters",
                ]
            )

            for line in data:

                if (not line) or (not line['tconst'].startswith('tt')):
                    continue

                movie = Movie.objects.filter(imdb_id=line['tconst']).first()

                person = Person.objects.filter(imdb_id=line['nconst']).first()

                if (not person) or (not movie):
                    continue

                person_movie_data = {
                    "ordering": int(line['ordering']),
                    "category": line['category'],
                    "job": None if line['job'] == "\\N" else line['job'],
                    "characters": None if line['characters'].startswith("\\N") else json.loads(line['characters']),
                }

                PersonMovie.objects.get_or_create(movie=movie, person=person, defaults=person_movie_data)
