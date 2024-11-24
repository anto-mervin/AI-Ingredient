def generate_prompt(recipe_name):

    
    prompt = f"""
Act as a programmer who is passionate about cooking. When given the recipe name "{recipe_name}" as input, 
generate a JSON structure containing the ingredients required for that recipe.

Each ingredient should include its name, quantity (if applicable), and unit (if applicable). Ensure the output 
is strictly in JSON format and is easy to understand.

The output format should look like this:
{{
    "recipe": "{recipe_name}",
    "ingredients": [
        {{ "name": "ingredient 1", "quantity": "value", "unit": "unit" }},
        {{ "name": "ingredient 2", "quantity": "value", "unit": "unit" }}
    ]
}}

For example, if the recipe name is "Tomato Rice", the output should be:
{{
    "recipe": "Tomato Rice",
    "ingredients": [
        {{ "name": "Rice", "quantity": 1, "unit": "cup" }},
        {{ "name": "Tomatoes", "quantity": 2, "unit": "medium" }},
        {{ "name": "Onion", "quantity": 1, "unit": "medium" }},
        {{ "name": "Green Chillies", "quantity": 2, "unit": "small" }},
        {{ "name": "Oil", "quantity": 2, "unit": "tablespoons" }},
        {{ "name": "Salt", "quantity": "to taste", "unit": null }}
    ]
}}

Generate the JSON structure for the recipe "{recipe_name}".
"""
    return prompt