from django.contrib import admin
from .models import Category, Tag, News, Slider

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(News)
admin.site.register(Slider)
