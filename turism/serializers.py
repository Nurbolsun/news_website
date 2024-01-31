from rest_framework import serializers

from .models import (
    HomePage, Region,
    Place, Category,
    PlaceImage, Month,
    Traveller, Video,
)


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = (
            'title',
            'description',
        )


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            'id',
            'title',
            'video_url'
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
            'short_description',
        )


class RegionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = (
            'id',
            'name',
            'image',
            'description',
        )


class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = (
            'id',
            'name',
            'image',
        )


class TravellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traveller
        fields = (
            'id',
            'name',
            'image',
        )


class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ('image',)


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
            'name',
            'image'
        )


class PlaceSerializer(serializers.ModelSerializer):
    images = PlaceImageSerializer(many=True, read_only=True)
    # months = MonthSerializer(many=True, read_only=True)
    # region = RegionSerializer(read_only=True)
    # categories = CategorySerializer(many=True)
    class Meta:
        model = Place
        fields = (
            'id',
            'name',
            'address',
            'phone_number',
            'images',
            'description',
            # 'months',
            # 'categories',
            # 'region'
        )
