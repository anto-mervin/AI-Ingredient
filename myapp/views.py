from django.shortcuts import render, redirect
from django.http import request


# Create your views here.
def home(request):
    return render(request, 'home.html')

def ai_recipe(request):
    return render(request, 'ai_recipe.html')