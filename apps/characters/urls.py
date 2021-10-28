from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path('/', views.characters, name='characters'),
    path('spiderman/', views.spiderman, name='spiderman'),
]