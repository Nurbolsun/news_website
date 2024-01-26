from rest_framework import serializers
from .models import News, Category, Tag, Author


class NewsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'description']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']