from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand

from app.models import Movie


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Movie()

        for i in range(100):
            # not str type, Path type
            image_path = settings.BASE_DIR / "app" / "assets" / "baby1.jpg"
            with image_path.open("rb") as f:  # read binary
                # f  # file object
                file = File(f)

                movie = Movie()
                movie.name = f"영화 #{i+2}"
                movie.poster.save(image_path.name, file, save=False)
                movie.save()

            print(f"current : {i}", end="\r", flush=True)

        print()
        print("Ended")
