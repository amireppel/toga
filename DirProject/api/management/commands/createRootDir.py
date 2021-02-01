from django.core.management.base import BaseCommand, CommandError
from api.models import Directory

class Command(BaseCommand):
    help = 'create the root directory for the project: python manage.py'
    def add_arguments(self, parser):
         parser.add_argument('name',type=str)


    def handle(self, *args, **options):
        name = options.get('name', 'Root')
        BaseDirectory = Directory( name = name)        
        BaseDirectory.save()
        print('base directory is: ', BaseDirectory)