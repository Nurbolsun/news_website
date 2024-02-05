from django.urls import path

from news.views import *

urlpatterns = [
    path('slider/', MainAPIView.as_view(),name='slider'),
    path('newses/', AllNewsAPIView.as_view(), name='all-news'),
    path('category/', CategoryViewSet.as_view({'get': 'list'}), name='all-categories'),
    path('category/<int:pk>', CategoryViewSet.as_view({'get': 'retrieve'})),
    path('category/create/', CategoryViewSet.as_view({'post': 'create'})),
    path('tag/<int:pk>', TagViewSet.as_view({'get': 'retrieve'})),
    path('tag/', TagViewSet.as_view({'get': 'list'})),
    path('tag/create/', TagViewSet.as_view({'post': 'create'})),

    path('news/', NewsAPIList.as_view()),
    path('news/<int:pk>', NewsAPIUpdate.as_view()),
    path('news/delete/<int:pk>', NewsAPIDestroy.as_view()),

]
