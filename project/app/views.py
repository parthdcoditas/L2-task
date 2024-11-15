from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .service import rewrite_text
import json

@csrf_exempt
def rewrite_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            text = data.get("text", "")
            
            if not text:
                return JsonResponse({"error": "Text is required"}, status=400)
            
            formal_text = rewrite_text(text, "formal",temperature=0.2)
            casual_text = rewrite_text(text, "casual",temperature=0.9)
            motivational_text = rewrite_text(text, "motivational",temperature=0.6)
            
            return JsonResponse({
                "formal": formal_text,
                "casual": casual_text,
                "motivational": motivational_text
            })

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)
