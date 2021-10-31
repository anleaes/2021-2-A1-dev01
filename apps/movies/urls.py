from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies, name='movies'),
    path('black_widow_movie/', views.black_widow_movie, name='black_widow_movie'),
]