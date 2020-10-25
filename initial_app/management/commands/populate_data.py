from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Populating database.'

    def handle(self, *args, **options):
        call_command('loaddata', 'users.json')
        self.stdout.write(self.style.SUCCESS('Successfully created users'))
        call_command('loaddata', 'activities_periods.json')
        self.stdout.write(self.style.SUCCESS('Successfully created activities periods'))
        call_command('loaddata', 'profile.json')
        self.stdout.write(self.style.SUCCESS('Successfully created profile.'))
                

        self.stdout.write(self.style.SUCCESS('Successfully created everything.'))
