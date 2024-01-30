from django.urls import path
from my_app.views import CategoryRetrieveAPIView, TagRetrieveAPIView, AllCategoryAPIView, \
    AllNewsAPIView, MainAPIView, NewsDetailView, NewsCreateView, CategoryCreateView

urlpatterns = [
    path('', MainAPIView.as_view()),
    path('news/', AllNewsAPIView.as_view(), name='all-news'),
    path('category/', AllCategoryAPIView.as_view(), name='all-categories'),
    path('category/<int:pk>', CategoryRetrieveAPIView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('tag/<int:pk>', TagRetrieveAPIView.as_view()),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-detail'),
    path('news/create/', NewsCreateView.as_view(), name='Создать Новости'),
]