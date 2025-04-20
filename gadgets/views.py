from rest_framework import generics
from .models import Gadget
from .serializers import GadgetSerializer
import requests
import json
import os
from django.http import JsonResponse
from django.conf import settings

class GadgetList(generics.ListAPIView):
    serializer_class = GadgetSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category:
            return Gadget.objects.filter(category__icontains=category)
        return Gadget.objects.all()

class GadgetDetail(generics.RetrieveAPIView):
    queryset = Gadget.objects.all()
    serializer_class = GadgetSerializer


def get_tech_news(request):
    api_key = os.environ.get('NEWS_API_KEY')  # Access the API key from the environment variable 
    api_url = 'https://newsapi.org/v2/top-headlines?category=technology&language=en'  # Replace with the actual API endpoint

    try:
        response = requests.get(api_url, params={'apiKey': api_key})
        response.raise_for_status()  # Raise an exception for bad status codes
        news_data = response.json()
        print(news_data)  # Debugging line to check the response data
        return JsonResponse(news_data)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'Failed to fetch news: {str(e)}'}, status=500)
