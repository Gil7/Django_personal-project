from django.core.management.base import BaseCommand,CommandError
from apps.shortener.models import KirrURL
class Command(BaseCommand):
    help = "Refreshes all KirrURL shortcodes"
    def handle(slef,*args,**kwargs):
        return KirrURL.objects.refresh_shortcodes()