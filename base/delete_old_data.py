from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from base.models import Room, Message

class Command(BaseCommand):
    help = 'Delete all rooms and messages older than one year'

    def handle(self, *args, **kwargs):
        one_year_ago = timezone.now() - timedelta(days=365)

        # Delete messages older than one year
        deleted_messages, _ = Message.objects.filter(created__lt=one_year_ago).delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {deleted_messages} messages older than one year.'))

        # Delete rooms older than one year
        deleted_rooms, _ = Room.objects.filter(created__lt=one_year_ago).delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {deleted_rooms} rooms older than one year.'))
