from django.db import models
from parler.models import TranslatableModel, TranslatedFields



class AboutUsModel(TranslatableModel):
    """ Модель информации о товаре """

    activated = models.BooleanField(verbose_name="Активирован", default=False)

    translations = TranslatedFields(
        title = models.CharField(verbose_name="Заголовок", max_length=200),
        text = models.TextField(verbose_name="Текст", max_length=5000)
    )

    class Meta:
        verbose_name = "О компаниии"
        verbose_name_plural = "О компаниии"

    def __str__(self) -> str:
        return f'{self.title[:35]}...'