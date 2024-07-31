# CVE_Finder/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .openai_utils import get_chatgpt_response

@csrf_exempt  # Temporarily disable CSRF protection for testing (remove in production)


def cve_chatbot(request):
    # Handle GET request to render the HTML page
    if request.method == 'GET':
        return render(request, 'CVE_Finder/cve_chatbot.html')

    # Handle POST request for AJAX interactions
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message')
            if user_message:
                bot_response = get_chatgpt_response(user_message)
                return JsonResponse({'response': bot_response})
            return JsonResponse({'response': 'Error: No message provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'response': 'Error: Invalid JSON'}, status=400)

    return JsonResponse({'response': 'Error: Invalid request'}, status=400)
