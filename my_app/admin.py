from django.contrib import admin
from .models import Category, Author, Tag, News,Slider

# Register your models here.

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(News)
admin.site.register(Slider)
