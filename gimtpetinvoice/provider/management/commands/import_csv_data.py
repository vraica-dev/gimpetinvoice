import csv
from django.core.management.base import BaseCommand, CommandParser
from django.apps import apps


class Command(BaseCommand):
    help = 'used for importing data via manage.py'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--csv_file', type=str, help="Path to the file.")
        parser.add_argument('--dbmodel', type=str, help="DB Model name.")
        parser.add_argument('--appmodule', type=str, help="Module name.")

    def handle(self, *args, **kwargs):
        file_path = kwargs['csv_file']
        dbmodel = kwargs['dbmodel']
        app = kwargs['appmodule']

        model = apps.get_model(app, dbmodel)
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            entries_created = 0

            for row in reader:
                model.objects.create(**row)
                entries_created += 1
                
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {entries_created} entries.'))
