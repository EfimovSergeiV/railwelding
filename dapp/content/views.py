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



class AboutUsView(APIView):
    """ Выдача информации о компании """
    queryset = AboutUsModel.objects.filter(activated=True)
    serializer_class = AboutUsSerializer

    def get(self, request):
        lang = get_language_from_request(request)        
        qs = AboutUsModel.objects.language(lang).get(id=1)
        serializer = self.serializer_class(qs, context={'request': request})

        return Response(serializer.data)