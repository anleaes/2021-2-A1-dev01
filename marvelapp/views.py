from django.shortcuts import render

# Create your views here.
def home(request):
    template_name ='core/home.html'
    context = {}
    return render(request, template_name, context)

def characters(request):
    template_name ='marvelapp/characters/characters.html'
    context = {}
    return render(request, template_name, context)

def spiderman(request):
    template_name ='marvelapp/characters/spiderman.html'
    context = {}
    return render(request, template_name, context)

def movies(request):
    template_name ='marvelapp/movies/movies.html'
    context = {}
    return render(request, template_name, context)