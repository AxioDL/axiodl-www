from django.core.management import BaseCommand, call_command, load_command_class
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "DEV COMMAND: Fill database with a set of data for testing purposes"

    def handle(self, *args, **options):
        call_command('migrate')
        call_command('loaddata', 'page_initial', 'board_initial')

        admin = User.objects.get(username='admin')
        if admin and admin.password == 'password':
            print('Found admin with unhashed, hasing password...')
            admin.set_password(admin.password)
            admin.save()
            print('Done!')
        else:
            print('Admin password already hashed, redundant call to initdata?')
