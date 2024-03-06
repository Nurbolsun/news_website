from django.contrib import admin
from django.contrib.admin import ModelAdmin
from solo.admin import SingletonModelAdmin
from django.utils.safestring import mark_safe

from turism.models import (
    HomePage, Region,
    Place, Category,
    PlaceImage, Month,
    Traveller, Video,
    Commentary, Feedback
)


@admin.register(HomePage)
class HomePageAdmin(SingletonModelAdmin):
    list_display = (
        'title',
        'id',
        'description',
        )


@admin.register(Video)
class VideoAdmin(SingletonModelAdmin):
    list_display = (
        'title',
        'id',
        'video_url',
        )


@admin.register(Region)
class RegionAdmin(ModelAdmin):
    list_display = (
        'name',
        'id',
        'image_show',
        'short_description',
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
        'title',
        'description',
        'img_show',
        'caption',
        'page',
        'title_2',
        'page_2',
        'title_3',
        'page_3',
        'title_4',
        'page_4',
        'title_5',
        'page_5',
    )

    def img_show(self, obj):
        if obj.img:
            return mark_safe("<img src='{}' width='60' />".format(obj.img.url))
        return 'None'
    img_show.__name__ = 'Фотография'


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1


@admin.register(PlaceImage)
class PlaceImageAdmin(ModelAdmin):
    list_display = (
        'id',
        'place',
        'image_show',
    )

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return 'None'
    image_show.__name__ = 'Изображение'


@admin.register(Month)
class MonthAdmin(ModelAdmin):
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


@admin.register(Traveller)
class TravellerAdmin(ModelAdmin):
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
    filter_horizontal = ('months',)
    inlines = [PlaceImageInline]
    list_display = (
        'name',
        'id',
        'address',
        'phone_number',
        'image_show',
        'description',
        'months',
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

    def months(self, obj):
        return ", ".join([month.name for month in obj.months.all()])
    months.short_description = 'Месяц'


@admin.register(Commentary)
class CommentaryAdmin(ModelAdmin):
    list_display = (
        'id',
        'title',
        'image',
        'description',
        'link',
    )

    def image(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return 'None'
    image.__name__ = 'Фотография'


@admin.register(Feedback)
class FeedbackAdmin(ModelAdmin):
    list_display = (
        'id',
        'get_user_name',
        'comment',
        'created_at'
    )

    def get_user_name(self, obj):
        return obj.user.username if obj.user else "Anonymous"

    get_user_name.short_description = 'User'