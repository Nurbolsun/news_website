from django.contrib import admin
from django.contrib.admin import ModelAdmin
from solo.admin import SingletonModelAdmin
from django.utils.safestring import mark_safe

from turism.models import HomePage, Region, Place, Category


@admin.register(HomePage)
class HomePageAdmin(SingletonModelAdmin):
    list_display = (
        'title',
        'id',
        'description',
        )


@admin.register(Region)
class RegionAdmin(ModelAdmin):
    list_display = (
        'name',
        'id',
        'image_show',
        'description',
    )
    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return 'None'
    image_show.__name__ = 'Фотография'


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
        'image_show',
    )
    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return 'None'
    image_show.__name__ = 'Фотография'


@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    list_display = (
        'name',
        'id',
        'address',
        'phone_number',
        'image_show',
        'description',
        'month',
        'region',
        'categories',
    )
    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return 'None'
    image_show.__name__ = 'Фотография'

    def categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])

    categories.short_description = 'Категории'