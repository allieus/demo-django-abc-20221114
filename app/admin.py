from django.contrib import admin
from app.models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
  pass
