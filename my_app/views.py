from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .models import News, Category, Tag, Author
from my_app.serializer import NewsListSerializers, CategoryListSerializer, TagListSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework import serializers


# Create your views here.

# class NewsListAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         from my_app.models import Category
#         print(type(self.request.query_params["category"]))
#         print(Category.objects.all()[0])
#         news = News.objects.filter(category=3)
#         news_json = NewsListSerializers(news, many=True)
#         return Response(data=news_json.data)

class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers


class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

    def post(self, request):
        serializer = AllCategoryAPIView(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        # Получаем данные из каждой модели
        category = Category.objects.all()
        news = News.objects.all()
        last_news = News.objects.all()
        if last_news.count() > 5:
            last_news = last_news.order_by('-id')[:5]
        else:
            last_news = News.objects.all()

        most_viewed_news = News.objects.all().order_by('-count_views')[:1]
        result_most_views = []

        for news_item in most_viewed_news:
            result_most_views.append({
                'category': news_item.category,
                'title': news_item.title,
                'description': news_item.description,
                'photo': news_item.photo,
                'count_views': news_item.count_views
            })
        category_serializer = CategoryListSerializer(category, many=True)
        news_serializer = NewsListSerializers(news, many=True)
        last_news_serializer = NewsListSerializers(last_news, many=True)
        most_viewed_news_serializer = NewsListSerializers(result_most_views, many=True)

        # Данные для категорий
        data_category = {'Категории': {'category1': category_serializer.data}}
        data_category['Категории'].update({'news': news_serializer.data})

        # Данные для популярных новостей
        data_popular_news = {'Популярные новости': {'category1': category_serializer.data}}
        data_popular_news['Популярные новости'].update({'news': most_viewed_news_serializer.data})

        # Данные для Последние новости
        data_latest_news = {'Последние новости': {'category1': category_serializer.data}}
        data_latest_news['Последние новости'].update({'news': last_news_serializer.data})

        # Общий результат
        result = [data_category, data_popular_news, data_latest_news]

        return Response(result)


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
