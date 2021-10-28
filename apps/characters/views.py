from django.shortcuts import render

# Create your views here.

def characters(request):
    template_name ='characters/characters.html'
    context = {}
    return render(request, template_name, context)

def spiderman(request):
    template_name ='characters/spiderman.html'
    context = {}
    return render(request, template_name, context)