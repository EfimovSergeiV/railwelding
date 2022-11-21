from django.db import models
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields


class ProductModel(TranslatableModel):
    """ Модель товара каталога """

    translations = TranslatedFields(
        name = models.CharField(verbose_name="Наименование", max_length=300),
        description = models.TextField(verbose_name="Описание", max_length=5000)
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name