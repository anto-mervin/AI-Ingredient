import google.generativeai as genai
import prompt
import json

genai.configure(api_key="AIzaSyDB9Xerpu6YhwejJsUVmZsUVmLV1RB8lsk")

model = genai.GenerativeModel("gemini-1.5-flash")

def json_response(response):
    # Remove the marker
    formatted_string = response.text.splitlines()[1:-1]  # Skip the first line (marker)
    cleaned_response = '\n'.join(formatted_string).strip()

    # Create a valid JSON array
    cleaned_response = '[' + cleaned_response + ']'

    # Remove trailing commas if present
    cleaned_response = cleaned_response.replace(",]", "]")  # Removes trailing comma before closing bracket

    # print("Cleaned Response:\n", cleaned_response, '\n')

    # Parse the cleaned_response string to a list of dictionaries
    try:
        api_response = json.loads(cleaned_response)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        api_response = []
    return api_response


def generate_ingredients(recipe):

    prompt_ = prompt.generate_prompt(recipe)

    refined_prompt = [
        {
            'role': 'user',
            'parts': [prompt_]
        }
    ]

    response = model.generate_content(refined_prompt)

    jsonresponse = json_response(response)


    print(jsonresponse)
    return jsonresponse


# generate_ingredients('tomato rice')