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
    priority = models.IntegerField(verbose_name="Приоритет выдачи", default=50)
    parent = TreeForeignKey('self', verbose_name="Вложенность", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    slug = models.SlugField(blank=False, default='', max_length=300)

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
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="category")

    translations = TranslatedFields(
        name = models.CharField(verbose_name="Наименование", max_length=300),
        description = models.TextField(verbose_name="Описание", max_length=5000)
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name



class ServiceModel(TranslatableModel):
    """ Модель списка услуг """

    activated = models.BooleanField(verbose_name="Активирован", default=False)
    priority = models.IntegerField(verbose_name="Приоритет выдачи", default=50)

    translations = TranslatedFields(
        name = models.CharField(verbose_name="Наименование", max_length=300),
        description = models.TextField(verbose_name="Описание", max_length=5000)
    )

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"

    def __str__(self):
        return self.name