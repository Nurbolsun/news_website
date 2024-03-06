from rest_framework import serializers

from .models import (
    HomePage, Region,
    Place, Category,
    PlaceImage, Month,
    Traveller, Video,
    Commentary, Feedback
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
            'title',
            'img',
            'description',
        )

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'description',
            'img',
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


class FeedbackSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Feedback
        fields = (
            'id',
            'user_name',
            'comment',
            'created_at'
        )

    def get_user_name(self, obj):
        return obj.user.username if obj.user else "Anonymous"

