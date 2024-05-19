import requests

def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None



def get_citations(request):
    api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    data = fetch_data_from_api(api_url)
    
    if data:
        print("API Data:", data)  # Debugging print statement

        if "data" in data and "data" in data["data"]:
            processed_data = process_responses(data["data"]["data"])
            print("Processed Data:", processed_data)  # Debugging print statement
            
            # Format the output as required
            citations_output = f"citations = {processed_data}"
            return JsonResponse({"data": citations_output}, safe=False)
        else:
            print("Invalid data format received:", data)  # Debugging print statement
            return JsonResponse({"error": "Invalid data format from API", "data": data}, status=500)
    else:
        return JsonResponse({"error": "Failed to fetch data from API"}, status=500)


def process_responses(data):
    all_citations = []
    for item in data:
        response = item['response']
        sources = item['source']
        print("Response:", response)  # Debugging print statement
        print("Sources:", sources)  # Debugging print statement
        citations = find_citations(response, sources)
        all_citations.extend(citations)
    print("All Citations:", all_citations)  # Debugging print statement
    return all_citations
