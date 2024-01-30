from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .models import News, Category, Tag, Author
from my_app.serializer import NewsListSerializers, CategoryListSerializer, TagListSerializer
from rest_framework.generics import RetrieveAPIView


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
        data = {}

        # Получаем данные из каждой модели
        category = Category.objects.all()
        news = News.objects.all()

        category_serializer = CategoryListSerializer(category, many=True)
        news_serializer = NewsListSerializers(news, many=True)

        data['category1'] = category_serializer.data
        data['news1'] = news_serializer.data

        return Response(data)


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
