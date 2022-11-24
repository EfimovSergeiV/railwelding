from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

from .models import (
    AboutUsModel,
)


class AboutUsSerializer(TranslatableModelSerializer):
    """ Сериализатор страницы о компании """

    class Meta:
        model = AboutUsModel
        fields = ('title', 'text')