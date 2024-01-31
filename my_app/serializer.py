from rest_framework import serializers
from .models import News, Category, Tag, Slider


class NewsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'category', 'title', 'description', 'photo',
                  'created_at', 'updated_at', 'tag', 'count_views', 'count_likes']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'