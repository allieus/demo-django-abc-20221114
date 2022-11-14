from django.urls import path

from app import views

urlpatterns = [
    path('', views.index),
    path("<int:pk>/", views.movie_detail),
    path("<int:movie_pk>/comments/new/", views.comment_new),
    path("<int:movie_pk>/comments/<int:pk>/edit/", views.comment_edit),
]
