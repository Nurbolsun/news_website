from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import HomePage, Region, Place, Category
from .serializers import (
    HomePageSerializer, RegionSerializer,
    RegionNameSerializer, CategorySerializer,
    PlaceSerializer, PlaceIncompleteSerializer,
)


class HomePageView(APIView):
    def get(self, request, *args, **kwargs):
        home_page = HomePage.objects.get()
        serializer = HomePageSerializer(home_page)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegionNameListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionNameSerializer


class RegionListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionDetailView(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PlaceListView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceIncompleteListView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceIncompleteSerializer


class PlaceDetailView(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

