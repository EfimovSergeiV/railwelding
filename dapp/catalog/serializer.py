from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

from .models import (
    CategoryModel,
    ProductModel,
)



class CategorySerializer(TranslatableModelSerializer):
    """ Сериализатор категорий """
    translations = TranslatedFieldsField(shared_model=CategoryModel)
    
    class Meta:
        model = CategoryModel
        fields = ('translations',)


class ProductSerializer(TranslatableModelSerializer):
    """ Сериализатор товаров """
    translations = TranslatedFieldsField(shared_model=ProductModel)
    
    class Meta:
        model = ProductModel
        fields = ('id', 'translations',)