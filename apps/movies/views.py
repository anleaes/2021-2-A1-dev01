from django.shortcuts import render

# Create your views here.

def movies(request):
    template_name ='movies/movies.html'
    context = {}
    return render(request, template_name, context)

def black_widow_movie(request):
    template_name ='movies/black_widow_movie.html'
    context = {}
    return render(request, template_name, context)
