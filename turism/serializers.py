from rest_framework import serializers

from .models import HomePage, Region, Place, Category


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = (
            'title',
            'description',
        )


class RegionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = (
            'id',
            'name',
        )

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = (
            'id',
            'name',
            'image',
            'description',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'image',
        )

class PlaceIncompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            'id',
            'image',
            'name',
            'description',
        )


class PlaceSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    categories = CategorySerializer(many=True)
    class Meta:
        model = Place
        fields = (
            'id',
            'name',
            'address',
            'phone_number',
            'image',
            'description',
            'month',
            'categories',
            'region'
        )
