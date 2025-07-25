import time
from django.db import OperationalError
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management.base import BaseCommand
from pprint import pprint




class Command(BaseCommand):

    def handle(self, *args, **options):
        """Command to pause execution until database is available"""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                # print( Psycopg2Error, OperationalError)
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!')) 
       