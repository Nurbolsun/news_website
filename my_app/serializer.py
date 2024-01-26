from rest_framework import serializers
from .models import News, Category, Tag, Author


class NewsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'author', 'category', 'title', 'description', 'photo',
                  'created_at', 'updated_at', 'tag', 'count_views']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']