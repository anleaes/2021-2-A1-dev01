from django.shortcuts import render

# Create your views here.
def home(request):
    template_name ='marvelapp/home.html'
    context = {}
    return render(request, template_name, context)

def spiderman(request):
    template_name ='marvelapp/characters/spiderman.html'
    context = {}
    return render(request, template_name, context)