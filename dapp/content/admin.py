from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from parler.forms import TranslatedField
from parler.admin import TranslatableAdmin, TranslatableModelForm, TranslatableTabularInline

from .models import (
    AboutUsModel,
)


class AboutUsForm(TranslatableModelForm):
    text = TranslatedField(label='Описание', widget=CKEditorWidget())


class AboutUsAdmin(TranslatableAdmin):
    form = AboutUsForm

    list_display = ('id', 'title', 'activated')
    list_display_links = ('id', 'title',)



admin.site.register(AboutUsModel, AboutUsAdmin)