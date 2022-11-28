"""
PS: Знаю про существование абстрактных классов,
Придумываю с головы, поэтому тут пока так!
"""

from django.db import models
from .managers import CategoryManager
from mptt.models import MPTTModel, TreeForeignKey
from parler.models import TranslatableModel, TranslatedFields



class CategoryModel(MPTTModel, TranslatableModel):
    """ 
    Модель категорий 
    Docs: https://django-parler.readthedocs.io/en/stable/advanced/mptt.html
    """

    activated = models.BooleanField(verbose_name="Активирован", default=False)
    parent = TreeForeignKey('self', verbose_name="Вложенность", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    slug = models.SlugField(verbose_name="Путь", blank=False, default='', max_length=300)

    translations = TranslatedFields(
        name = models.CharField(verbose_name="Наименование", max_length=300),
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    objects = CategoryManager()

    # class MPTTMeta:
    #     order_insertion_by = ('activated',)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)



class ProductModel(TranslatableModel):
    """ Модель товара каталога """

    activated = models.BooleanField(verbose_name="Активирован", default=False)
    priority = models.IntegerField(verbose_name="Приоритет выдачи", default=50)
    category = models.ForeignKey(CategoryModel, verbose_name="Категория", on_delete=models.CASCADE, related_name="product_category")

    translations = TranslatedFields(
        name = models.CharField(verbose_name="Наименование", max_length=300),
        description = models.TextField(verbose_name="Описание", max_length=5000)
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class ProductAdvantagesModel(TranslatableModel):
    """ Модель преимуществ товаров """

    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="advantages_product")
    styles = models.CharField(verbose_name="Стили", max_length=500, null=True, blank=True, help_text="Стили TailwindCSS, которые будут добавлены к классу (https://tailwindcss.com)", )

    translations = TranslatedFields(
        text = models.CharField(verbose_name="Текст", max_length=1000)
    )

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    def __str__(self):
        return self.product.name


class ProductPropertiesModel(TranslatableModel):
    """ Модель свойств товара """

    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="properties_product")
    styles = models.CharField(verbose_name="Стили", null=True, blank=True, max_length=500, help_text="Стили TailwindCSS, которые будут добавлены к классу (https://tailwindcss.com)", )

    translations = TranslatedFields(
        text = models.CharField(verbose_name="Текст", max_length=1000),
        value = models.CharField(verbose_name="Значение", null=True, blank=True, max_length=1000)
    )
        
    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'

    def __str__(self):
        return self.product.name



class ServiceModel(TranslatableModel):
    """ Модель списка услуг """

    activated = models.BooleanField(verbose_name="Активирован", default=False)
    priority = models.IntegerField(verbose_name="Приоритет выдачи", default=50)
    category = models.ForeignKey(CategoryModel, verbose_name="Категория", on_delete=models.CASCADE, related_name="service_category")

    translations = TranslatedFields(
        name = models.CharField(verbose_name="Наименование", max_length=300),
        description = models.TextField(verbose_name="Описание", max_length=5000)
    )

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"

    def __str__(self):
        return self.name