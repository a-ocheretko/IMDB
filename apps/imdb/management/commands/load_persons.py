import os.path
from django.core.management.base import BaseCommand, CommandError
from apps.imdb.models import Person
import csv


class Command(BaseCommand):

    help = "Imports persons from tsv file"

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
                    "nconst",
                    "primaryName",
                    "birthYear",
                    "deathYear",
                    "primaryProfession",
                    "knownForTitles",
                ],
            )

            for line in data:

                if (not line) or (not line['nconst'].startswith('nm')):
                    continue

                person_data = {
                    "name": line['primaryName'],
                    "birth_year": None if line['birthYear'] == "\\N" else int(line['birthYear']),
                    "death_year": None if line['deathYear'] == "\\N" else int(line['deathYear']),
                }
                person, created = Person.objects.get_or_create(imdb_id=line['nconst'], defaults=person_data)

                if created:
                    Person.objects.filter(id=person.id).update(**person_data)
