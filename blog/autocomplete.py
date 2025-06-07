import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from decouple import config

# Configure Gemini
GOOGLE_API_KEY = config("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

@csrf_exempt
def autocomplete_blog(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('prompt', '')
        print("User input received:", user_input)
        if not user_input:
            return JsonResponse({'suggestion': ''})

        # Improve prompt for Gemini
        prompt = f"Continue this blog post with a plausible next phrase or sentence:\n\n{user_input}"

        try:
            response = model.generate_content(
                prompt,
                generation_config={
                    'max_output_tokens': 20,
                    'temperature': 0.7,
                    'top_p': 1.0
                },
                stream=False,
            )
            suggestion = response.text.strip()
            return JsonResponse({'suggestion': suggestion})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
