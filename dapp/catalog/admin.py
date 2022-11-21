from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from parler.admin import TranslatableAdmin, TranslatableModelForm
from parler.forms import TranslatedField

from catalog.models import ProductModel


class ProductForm(TranslatableModelForm):
    description = TranslatedField(label='Описание', widget=CKEditorWidget())


class ProductAdmin(TranslatableAdmin):
    form = ProductForm

    list_display = ('id', 'name',)
    fieldsets = (
        (None, {'fields': ('name',)}),
        (None, {'fields': ('description',)}),
    )


admin.site.register(ProductModel, ProductAdmin)