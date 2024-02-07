from rest_framework import serializers

from .models import (
    HomePage, Region,
    Place, Category,
    PlaceImage, Month,
    Traveller, Video, Commentary,
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
        fields = (
            'id',
            'image',
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
            'name',
            'image'
        )


class PlaceIncompleteWithRegionSerializer(serializers.ModelSerializer):
    region = RegionNameSerializer(read_only=True)

    class Meta:
        model = Place
        fields = (
            'id',
            'name',
            'image',
            'region',
        )


class PlaceSerializer(serializers.ModelSerializer):
    place_images = PlaceImageSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = (
            'id',
            'name',
            'address',
            'phone_number',
            'place_images',
            'description',
        )


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = (
            'id',
            'image',
            'title',
            'description',
            'link',
        )