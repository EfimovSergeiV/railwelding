from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from mptt.admin import DraggableMPTTAdmin
from mptt.forms import MPTTAdminForm
from parler.forms import TranslatedField
from parler.admin import TranslatableAdmin, TranslatableModelForm, TranslatableTabularInline

from catalog.models import (
    CategoryModel,
    ProductModel,
    ServiceModel,
    ProductAdvantagesModel,
    ProductPropertiesModel,
)



class CategoryAdminForm(MPTTAdminForm, TranslatableModelForm):
    pass


class CategoryAdmin(TranslatableAdmin, DraggableMPTTAdmin):
    form = CategoryAdminForm

    list_display = ('tree_actions', 'indented_title', 'activated',)
    list_editable = ('activated',)
    fieldsets = (
        (None, {'fields': (('parent','activated'),('name', 'slug',),)}),
    )

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}



class ProductAdvantagesInlines(TranslatableTabularInline):
    model = ProductAdvantagesModel
    extra = 0

class ProductPropertiesInlines(TranslatableTabularInline):
    model = ProductPropertiesModel
    extra = 0


class ProductForm(TranslatableModelForm):
    description = TranslatedField(label='Описание', widget=CKEditorWidget())


class ProductAdmin(TranslatableAdmin):
    form = ProductForm

    list_display = ('id', 'name', 'activated')
    list_display_links = ('id', 'name',)
    list_editable = ('activated',)
    search_fields = ('id', 'name',)
    list_filter = ('activated',)
    ordering = ('id',)
    fieldsets = (
        (None, {'fields': (('category',), ('name', 'priority', 'activated'), ('description',),)}),
    )
    inlines = (
        ProductAdvantagesInlines,
        ProductPropertiesInlines,
    )



class ServiceForm(TranslatableModelForm):
    description = TranslatedField(label='Описание', widget=CKEditorWidget())


class ServiceAdmin(TranslatableAdmin):
    form = ServiceForm

    list_display = ('id', 'name', 'activated',)
    list_display_links = ('id', 'name',)
    list_editable = ('activated',)
    search_fields = ('id', 'name',)
    list_filter = ('activated',)
    ordering = ('id',)
    fieldsets = (
        (None, {'fields': (('category',), ('name', 'priority', 'activated'), ('description',),)}),
    )

admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(ProductModel, ProductAdmin)
admin.site.register(ServiceModel, ServiceAdmin)