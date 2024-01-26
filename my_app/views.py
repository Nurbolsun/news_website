from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import News, Category, Tag, Author
from my_app.serializer import NewsListSerializers, CategoryListSerializer, TagListSerializer
from rest_framework.generics import RetrieveAPIView


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