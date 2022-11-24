from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils.translation import get_language_from_request

from .models import (
    AboutUsModel
)
from .serializer import (
    AboutUsSerializer
)

"""
{
    'Content-Length': '', 'Content-Type': 'text/plain', 
    'Connection': 'keep-alive', 
    'Pragma': 'no-cache', 
    'Cache-Control': 'no-cache', 
    'Upgrade-Insecure-Requests': '1', 
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36', 
    'Sec-Fetch-Site': 'same-origin', 
    'Sec-Fetch-Mode': 'navigate', 
    'Sec-Fetch-User': '?1', 
    'Sec-Fetch-Dest': 'document', 
    'Sec-Ch-Ua': '"Google Chrome";v="107", 
    "Chromium";v="107", 
    "Not=A?Brand";v="24"', 
    'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '"Linux"', 
    'Referer': 'http://localhost:3000/ru', 'Accept-Encoding': 'gzip, deflate', 
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 
    'Cookie': '_ga=GA1.1.1433435990.1664344016; _ga_9T3RH9YGQV=GS1.1.1669033431.7.1.1669039277.0.0.0;
     i18n_redirected=ru; Accept-Language=en; lang=ru', 'Accept': 'application/json, text/plain, */*', 'Host': '127.0.0.1:8000'}

"""


class AboutUsView(APIView):
    """ Выдача информации о компании """
    queryset = AboutUsModel.objects.filter(activated=True)
    serializer_class = AboutUsSerializer

    def get(self, request):
        lang = get_language_from_request(request)
        print('\n\n\n\n\n\n\n\n\n')
        print(lang)
        print(request.headers)
        
        qs = AboutUsModel.objects.language(lang).get(id=1)

        serializer = self.serializer_class(qs, context={'request': request})
        print(serializer.data)
        print('\n\n\n\n\n\n\n')
        return Response(serializer.data)