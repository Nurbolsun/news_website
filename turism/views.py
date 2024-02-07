from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    HomePage, Region,
    Place, Category,
    Month, Traveller,
    Video, Commentary
)
from .serializers import (
    HomePageSerializer, RegionSerializer,
    RegionNameSerializer, RegionSerializer,
    RegionDetailSerializer, CategorySerializer,
    PlaceSerializer, PlaceIncompleteSerializer,
    MonthSerializer, TravellerSerializer,
    VideoSerializer, PlaceIncompleteWithRegionSerializer, CommentarySerializer
)


class HomePageView(APIView):
    def get(self, request, *args, **kwargs):
        home_page = HomePage.objects.get()
        serializer = HomePageSerializer(home_page)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VideoView(APIView):
    def get(self, request):
        try:
            video = Video.objects.first()
            serializer = VideoSerializer(video)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Video.DoesNotExist:
            return Response({'error': 'Видео не найдено'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PlacesByCategoryView(APIView):
    def get(self, request, category_id):
        try:
            places = Place.objects.filter(categories__id=category_id)
            serializer = PlaceIncompleteWithRegionSerializer(places, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RegionNameListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionNameSerializer


class RegionListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionDetailView(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionDetailSerializer


class PlacesByRegionView(APIView):
    def get(self, request, region_id):
        try:
            places = Place.objects.filter(region__id=region_id)
            serializer = PlaceIncompleteSerializer(places, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Region.DoesNotExist:
            return Response({'error': 'Регион не найден'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PLacesByTravellerView(APIView):
    def get(self, request, traveller_id):
        try:
            traveller = Traveller.objects.get(id=traveller_id)
            places = traveller.places.all()
            serializer = PlaceIncompleteWithRegionSerializer(places, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Traveller.DoesNotExist:
            return Response({'error': 'Путешествие не найдено'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PlacesByMonthView(APIView):
    def get(self, request, month_id):
        try:
            month = Month.objects.get(id=month_id)
            places = month.places.all()
            serializer = PlaceIncompleteWithRegionSerializer(places, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Month.DoesNotExist:
            return Response({'error': 'Месяц не найден'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MonthListView(generics.ListAPIView):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer


class TravellerListView(generics.ListAPIView):
    queryset = Traveller.objects.all()
    serializer_class = TravellerSerializer


class PlaceListView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceIncompleteWithRegionSerializer


class PlaceDetailView(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class CommentaryListView(generics.ListAPIView):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer