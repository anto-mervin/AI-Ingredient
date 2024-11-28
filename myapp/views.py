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

        # Check if the response contains an error
        if "error" in ingredients[0]:
            error_message = ingredients[0]["error"]
            print("\nError:", error_message)
            return render(
                request,
                'ai_recipe.html',
                {
                    'recipes': None,
                    'matched_groceries': None,
                    'search_query': search_query,
                    'error_message': error_message,
                }
            )

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

