from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from mptt.admin import DraggableMPTTAdmin
from mptt.forms import MPTTAdminForm
from parler.forms import TranslatedField
from parler.admin import TranslatableAdmin, TranslatableModelForm

from catalog.models import ProductModel, ServiceModel, CategoryModel



class CategoryAdminForm(MPTTAdminForm, TranslatableModelForm):
    pass


class CategoryAdmin(TranslatableAdmin, DraggableMPTTAdmin):
    form = CategoryAdminForm

    list_display = ('tree_actions', 'indented_title', 'activated',)
    list_editable = ('activated',)

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}



class ProductForm(TranslatableModelForm):
    description = TranslatedField(label='Описание', widget=CKEditorWidget())


class ProductAdmin(TranslatableAdmin):
    form = ProductForm

    list_display = ('id', 'name', 'activated')
    list_editable = ('activated',)
    fieldsets = (
        (None, {'fields': (('name', 'priority', 'activated'),)}),
        (None, {'fields': ('description',)}),
    )



class ServiceForm(TranslatableModelForm):
    description = TranslatedField(label='Описание', widget=CKEditorWidget())


class ServiceAdmin(TranslatableAdmin):
    form = ServiceForm

    list_display = ('id', 'name', 'activated',)
    list_editable = ('activated',)
    fieldsets = (
        (None, {'fields': (('name', 'priority', 'activated'))}),
        (None, {'fields': ('description',)}),
    )

admin.site.register(
    CategoryModel, 
    CategoryAdmin
)
admin.site.register(ProductModel, ProductAdmin)
admin.site.register(ServiceModel, ServiceAdmin)