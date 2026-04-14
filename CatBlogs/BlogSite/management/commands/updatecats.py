from typing import Any
from django.core.management.base import BaseCommand, CommandParser
import pandas as pd
from BlogSite.models import Cat

class Command(BaseCommand):
    help = 'Import cats from cat CSV'

    def handle(self, *args, **kwargs):
        file_path = 'csv/cat.csv' 
        try:
            df = pd.read_csv(file_path)
            for index, row in df.iterrows():
                Cat.objects.create(
                    breed=row['breed'],
                    description=row['description'],
                    traits=row['traits'],
                    height=row['height'],
                    weight=row['weight'],
                    population=row['population']
                )
            self.stdout.write(self.style.SUCCESS('Successfully imported cats from CSV'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File not found. Please provide the correct file path'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))