from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import News
from my_app.serializer import NewsListSerializers
# Create your views here.


class NewsListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        news = News.objects.all()
        news_json = NewsListSerializers(news, many=True)
        return Response(data=news_json.data)


