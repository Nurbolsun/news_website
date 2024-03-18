from rest_framework import status, generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from news.serializers import NewsListSerializers, NewsCategoryListSerializer, TagListSerializer, SliderSerializer
from .models import News, NewsCategory, Tag, Slider


class NewsAPIList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers


class NewsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers
    permission_classes = (IsAuthenticated, )


class NewsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers


class NewsCategoryViewSet(viewsets.ModelViewSet):
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategoryListSerializer


class NewsByCategoryAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        category = get_object_or_404(NewsCategory, pk=pk)
        news = News.objects.filter(news_category=category)
        news_serializer = NewsListSerializers(news, many=True)
        return Response(news_serializer.data)


class SortNewsByDataAPI(APIView):
    def get(self, request, *args, **kwargs):
        last_news = News.objects.all().order_by('-created_at')[:5]
        last_news_serializer = NewsListSerializers(last_news, many=True)
        return Response(last_news_serializer.data)


class MostViewerNews(APIView):
    def get(self, request, *args, **kwargs):
        most_viewed_news = News.objects.all().order_by('-count_views')[:5]
        most_viewed_serializer = NewsListSerializers(most_viewed_news, many=True)
        return Response(most_viewed_serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class AllNewsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        news = News.objects.all()
        serializer = NewsListSerializers(news, many=True)
        return Response(serializer.data)


class SliderAPIViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


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
