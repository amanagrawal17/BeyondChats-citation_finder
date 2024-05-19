from django.http import JsonResponse
from .utils import fetch_data_from_api, process_responses

def get_citations(request):
    api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    data = fetch_data_from_api(api_url)
    
    if data:
        # print("API Data:", data)  # Debugging print statement

        if isinstance(data, list) or (isinstance(data, dict) and "results" in data):
            results = process_responses(data)
            return JsonResponse(results, safe=False)
        else:
            return JsonResponse({"data": data}, status=500)
    else:
        return JsonResponse({"error": "Failed to fetch data from API"}, status=500)
