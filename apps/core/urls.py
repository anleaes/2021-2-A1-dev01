from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('characters/', views.characters, name='characters'),
    path('spiderman/', views.spiderman, name='spiderman'),
    path('movies/', views.movies, name='movies'),
]