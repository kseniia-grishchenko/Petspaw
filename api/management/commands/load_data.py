import requests

from django.core.management.base import BaseCommand

from api.models import Breed, Image, Favourite, Vote


class Command(BaseCommand):
    """Django command that waits for database to be available"""

    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write('Adding Breeds!')

        data = requests.get("https://api.thedogapi.com/v1/breeds").json()
        for breed in data:
            Breed.objects.update_or_create(
                id=breed["id"],
                weight=breed["weight"]["metric"],
                height=breed["height"]["metric"],
                name=breed["name"],
                bred_for=breed.get("bred_for", None),
                breed_group=breed.get("breed_group", None),
                temperament=breed.get("temperament", None),
                origin=breed.get("origin", None),
                country_code=breed.get("country_code", None)
            )
            print(".", end="")

        self.stdout.write('Adding Images!')

        data = requests.get("https://api.thedogapi.com/v1/images/search?limit=100").json()
        for image in data:
            if image["breeds"]:
                Image.objects.update_or_create(
                    breed_id=image["breeds"][0]["id"],
                    url=image["url"],
                )
                print(".", end="")

        self.stdout.write(self.style.SUCCESS('Successfully added!'))
