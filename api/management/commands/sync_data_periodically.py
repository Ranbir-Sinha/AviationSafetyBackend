from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = 'Sync data from CSV file to database periodically'

    def handle(self, *args, **options):
        python_executable = 'python'
        manage_py_path = 'manage.py'
        schedule = '*/5 * * * *'
        full_command = f'{python_executable} {manage_py_path} sync_data'
        subprocess.run(["cron", f"job -s {schedule} {full_command}"])
