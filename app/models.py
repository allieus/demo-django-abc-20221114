from django.conf import settings
from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    # upload_to : 저장시점에 저장되는 폴더의 경로를 지정 (문자열 or 함수)
    poster = models.ImageField(upload_to="app/movies/%Y/%m/%d")

    def __str__(self):
        return self.name


# blank=False, null=False

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
