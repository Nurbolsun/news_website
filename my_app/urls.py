from django.urls import path
from my_app.views import *

urlpatterns = [
    path('slider/', MainAPIView.as_view()),
    path('news/', NewsViewSet.as_view({'get': 'list'}), name='all-news'),
    path('category/', CategoryViewSet.as_view({'get': 'list'}), name='all-categories'),
    path('category/<int:pk>', CategoryViewSet.as_view({'put': 'update'})),
    path('category/create/', CategoryCreateView.as_view()),
    path('tag/<int:pk>', TagRetrieveAPIView.as_view()),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-detail'),
    path('news/create/', NewsViewSet.as_view({'post': 'create'}), name='Создать Новости'),
]