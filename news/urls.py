from django.urls import path

from news.views import *

urlpatterns = [
    path('slider/', SliderAPIViewSet.as_view({'get': 'list'}), name='slider'),
    path('slider/<int:pk>', SliderAPIViewSet.as_view({'get': 'retrieve'})),

    path('news-category/', NewsCategoryViewSet.as_view({'get': 'list'}), name='all-categories'),
    path('news-category/<int:pk>', NewsCategoryViewSet.as_view({'get': 'retrieve'})),
    path('news-category/create/', NewsCategoryViewSet.as_view({'post': 'create'})),
    path('news-by-category/<int:pk>', NewsByCategoryAPIView.as_view(), name='news-by-category'),
    path('news-by-data/', SortNewsByDataAPI.as_view(), name='news-by-data'),
    path('news-by-view/', MostViewerNews.as_view(), name='news-by-view'),
    path('tag/<int:pk>', TagViewSet.as_view({'get': 'retrieve'})),
    path('tag/', TagViewSet.as_view({'get': 'list'})),
    path('tag/create/', TagViewSet.as_view({'post': 'create'})),

    path('news/', NewsAPIList.as_view()),
    path('news/<int:pk>', NewsDetailView.as_view()),
    path('news/delete/<int:pk>', NewsAPIDestroy.as_view()),

]
