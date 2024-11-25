from django.shortcuts import render, redirect
from django.http import request
from . import genai
import json
from django.conf import settings
import os




# Create your views here.
def home(request):
    return render(request, 'home.html')

def ai_recipe(request):

    search_query = request.GET.get('query', '')

    if search_query:

        print('\nRecipe:',search_query)
        ingredients = genai.generate_ingredients(search_query)
        print('\nIngredient:',ingredients)

        # Match groceries from your JSON file
        groceries_file = os.path.join(settings.BASE_DIR, 'myapp/static/grocery.json')
        with open(groceries_file, 'r') as file:
            grocery_data = json.load(file)

        groceries = []
        for category in grocery_data.values():
            groceries.extend(category)

        # Match ingredients with grocery items
        matched_items = []
        for ingredient in ingredients[0]['ingredients']:
            for grocery in groceries:
                if grocery['name'].lower() == ingredient['name'].lower():
                    matched_items.append(grocery)

        print('\nMatched Items:', matched_items)

        
        # Pass the matched grocery items to the template
        return render(
            request,
            'ai_recipe.html',
            {
                'recipes': ingredients,
                'matched_groceries': matched_items,
                'search_query': search_query,
            }
        )
    else:
        return render(request, 'ai_recipe.html', {'recipes': None, 'matched_groceries': None, 'search_query': ''})

# def ai_recipe(request):
#     search_query = request.GET.get('query', '')

#     if search_query:
#         print('\nRecipe:', search_query)
#         ingredients = genai.generate_ingredients(search_query)
#         print('\nIngredients:', ingredients)

#         # Match groceries from your JSON file
#         groceries_file = os.path.join(settings.BASE_DIR, 'myapp/static/grocery.json')
#         with open(groceries_file, 'r') as file:
#             grocery_data = json.load(file)

#         matched_groceries = []
#         for recipe in ingredients:
#             for ingredient in recipe['ingredients']:
#                 name = ingredient['name'].lower()
#                 for category, items in grocery_data.items():
#                     for item in items:
#                         if name in item['name'].lower():
#                             matched_groceries.append(item)

#         return render(
#             request,
#             'ai_recipe.html',
#             {
#                 'recipes': ingredients,
#                 'matched_groceries': matched_groceries,
#                 'search_query': search_query,
#             }
#         )
#     else:
#         return render(request, 'ai_recipe.html', {'recipes': None, 'matched_groceries': None, 'search_query': ''})
