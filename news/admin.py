from django.contrib import admin
from .models import NewsCategory, Tag, News, Slider

# Register your models here.

admin.site.register(NewsCategory)
admin.site.register(Tag)
admin.site.register(News)
admin.site.register(Slider)
