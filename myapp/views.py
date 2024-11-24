from django.shortcuts import render, redirect
from django.http import request
from . import genai


# Create your views here.
def home(request):
    return render(request, 'home.html')

def ai_recipe(request):

    search_query = request.GET.get('query', '')

    print('\nRecipe:',search_query)
    ingriedents = genai.generate_ingredients(search_query)
    print('\nIngredient:',ingriedents)

    
    return render(request, 'ai_recipe.html',{'recipes': ingriedents})