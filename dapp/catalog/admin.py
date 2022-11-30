from django.contrib import admin
from django.utils.safestring import mark_safe
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
    ProductImageModel,
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

class ProductImageInline(admin.TabularInline):
    model = ProductImageModel
    extra = 0


class ProductForm(TranslatableModelForm):
    description = TranslatedField(label='Описание', widget=CKEditorWidget())


class ProductAdmin(TranslatableAdmin):
    def preview_img(self, obj):
        return mark_safe('<img style="margin-right: -10vh" src="/files/%s" alt="Нет изображения" width="160" height="auto" />' % (obj.preview))
    preview_img.short_description = 'Изображение'

    form = ProductForm
    readonly_fields = ('preview_img', )
    list_display = ('id', 'name', 'activated')
    list_display_links = ('id', 'name',)
    list_editable = ('activated',)
    search_fields = ('id', 'name',)
    list_filter = ('activated',)
    ordering = ('id',)
    fieldsets = (
        (None, {'fields': (('category',), ('name', 'priority', 'activated'), ('description',), ('preview_img', 'preview',))}),
    )
    inlines = (
        ProductAdvantagesInlines,
        ProductPropertiesInlines,
        ProductImageInline,
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