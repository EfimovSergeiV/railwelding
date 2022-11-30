from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

from .models import (
    CategoryModel,
    ProductModel,
    ProductAdvantagesModel,
    ProductPropertiesModel,
)



class CategorySerializer(TranslatableModelSerializer):
    """ Сериализатор категорий """
    translations = TranslatedFieldsField(shared_model=CategoryModel)
    
    class Meta:
        model = CategoryModel
        fields = ('translations',)


class ProductAdvantagesInline(TranslatableModelSerializer):
    """ Вложенные поля преимуществ товара """

    class Meta:
        model = ProductAdvantagesModel
        fields = ('styles', 'product', 'text',)

class ProductPropertiesInline(TranslatableModelSerializer):
    """ Вложенные поля свойств товара """

    class Meta:
        model = ProductPropertiesModel
        fields = ('styles', 'text', 'value',)

class ProductSerializer(TranslatableModelSerializer):
    """ Сериализатор товаров """
    advantages_product = ProductAdvantagesInline(many=True)
    properties_product = ProductPropertiesInline(many=True)

    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'description', 'preview', 'advantages_product', 'properties_product')