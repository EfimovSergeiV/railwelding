from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from django.utils.translation import get_language_from_request

from .models import (
    CategoryModel,
    ProductModel,
)
from .serializer import (
    CategorySerializer,
    ProductSerializer,
)


class CategoryView(APIView):
    """ Выдача категорий каталога """
    queryset = CategoryModel.objects.filter(activated=True)
    serializer_class = CategorySerializer

    def get(self, request):
        qs_category = CategoryModel.objects.all()

        for qs in qs_category:
            print(qs)

        serializer = self.serializer_class(qs_category, context={'request': request})
        categories = serializer.data
        return Response(categories)


class ProductView(APIView):
    """ Выдача одного товара по id """

    queryset = ProductModel.objects.filter(activated=True)
    serializer_class = ProductSerializer

    def get(self, request, pk):

        lang = get_language_from_request(request)
        qs_product = self.queryset.language(lang).get(id=pk)
        serializer = self.serializer_class(qs_product, context={'request': request})

        return Response(serializer.data)


class AllProductView(APIView):
    """ Выдача всех товаров """

    queryset = ProductModel.objects.filter(activated=True)
    serializer_class = ProductSerializer

    def get(self, request):
        lang = get_language_from_request(request)
        qs_products = self.queryset.language(lang).all()
        serializer = self.serializer_class(qs_products, many=True, context={'request': request})

        return Response(serializer.data)
