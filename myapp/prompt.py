def generate_prompt(recipe_name):

    
    prompt = f"""
Act as a programmer who is passionate about cooking. When given the input "{recipe_name}", first check if the input is a valid food name. 
If the input is not a valid food name, respond with: 
"Please enter a valid food name."

If the input is a valid food name, generate a JSON structure containing the ingredients required for that recipe. 
Each ingredient should include its name, quantity (if applicable), and unit (if applicable). 
Ensure the output is strictly in JSON format and is easy to understand. 

Additionally, if the recipe includes 'Ginger-Garlic Paste', separate it into two distinct ingredients: 
one for 'Ginger' and one for 'Garlic', with appropriate quantities and units.

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
        {{ "name": "Ginger", "quantity": 1, "unit": "teaspoon" }},
        {{ "name": "Garlic", "quantity": 1, "unit": "teaspoon" }},
        {{ "name": "Salt", "quantity": "to taste", "unit": null }}
    ]
}}

Important Note: 
1. The **quantity** of each ingredient must always be represented as a string, even if it is a number.
2. Give all values as string datatype and don't use plural formal , give ingredient as raw form of vegatable or fruits or spices.
3. Generate the JSON structure for the recipe "{recipe_name}" if it's a valid food name, or return the error message if it's not.

"error": "Please enter a valid food name."

Make sure that the error should be in the json format where the key is the "error" and the value is "Please enter a valid food name."

"""

    return prompt