from rest_framework import status, generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from news.serializers import NewsListSerializers, CategoryListSerializer, TagListSerializer, SliderSerializer
from .models import News, Category, Tag, Slider
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.

class NewsAPIList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers
    # permission_classes = (IsAuthenticatedOrReadOnly, )


class NewsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers
    permission_classes = (IsAuthenticated, )


class NewsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers


class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class TagRetrieveAPIView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class AllCategoryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data)


class AllNewsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        news = News.objects.all()
        serializer = NewsListSerializers(news, many=True)
        return Response(serializer.data)


class MainAPIView(APIView):
    def get(self, request, *args, **kwargs):
        slider = Slider.objects.all()
        news = News.objects.all()

        slider_serializer = SliderSerializer(slider, many=True)
        news_serializer = NewsListSerializers(news, many=True)

        data_slider = slider_serializer.data

        for slider_item in data_slider:
            slider_item['news'] = news_serializer.data

        return Response(data_slider)


class NewsDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response({"detail": "News not found"}, status=status.HTTP_404_NOT_FOUND)

        news.count_views += 1
        news.save()

        serializer = NewsListSerializers(news)
        return Response(serializer.data, status=status.HTTP_200_OK)
