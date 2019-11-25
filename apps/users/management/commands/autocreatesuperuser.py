from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()
        email = settings.ADMIN_EMAIL
        username = settings.ADMIN_USERNAME
        password = settings.ADMIN_PASSWORD
        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS("Admin account created!"))
