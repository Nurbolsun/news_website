import pytz
from rest_framework import serializers

from .models import (
    HomePage, Region,
    Place, Category,
    PlaceImage, Month,
    Traveller, Video,
    Commentary, Feedback,
    ConsultationRequest
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
            'short_description',
            'description',
            'img_1',
            'img_2',
            'img_3',
            'description_1',
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


class TravellerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traveller
        fields = (
            'id',
            'name',
            'image',
            'img_2',
            'title',
            'description_1',
            'description_2',
            'img_3',
            'img_4',
            'img_5',
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
    created_at = serializers.SerializerMethodField()
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

    def get_created_at(self, obj):
        bishkek_timezone = pytz.timezone('Asia/Bishkek')
        created_at_bishkek = obj.created_at.astimezone(bishkek_timezone)
        return created_at_bishkek.strftime("%d-%m-%Y-%H:%M")

class ConsultationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationRequest
        fields = '__all__'
