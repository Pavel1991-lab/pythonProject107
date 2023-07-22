
from django.core.management import BaseCommand
from config import settings
settings.configure()
from catalog.models import Category
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalog.settings')


class Command(BaseCommand):

    def handle(self, *args, **options):
        category = [
            {'name': 'ягода', 'description': 'Фрукт'}
        ]

        cetegory_create = []
        for i in category:
            cetegory_create.append(
                Category(**i)
            )

        Category.objects.bulk_create(cetegory_create)