from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This command used for Category the data insert"

    def handle(self, *args: Any, **options: Any):

        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully Deleted the Data'))
  
        categories = ['Sports', 'Technology', 'Science', 'Art', 'Food']

        for categoryname in categories:
            Category.objects.create(
                name=categoryname,
            )

        self.stdout.write(self.style.SUCCESS('Successfully inserted the Data'))