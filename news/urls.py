from django.urls import path

from news.views import *

urlpatterns = [
    path('slider/', MainAPIView.as_view()),
    path('news/', AllNewsAPIView.as_view(), name='all-news'),
    path('category/', AllCategoryAPIView.as_view(), name='all-categories'),
    path('category/<int:pk>', CategoryRetrieveAPIView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('tag/<int:pk>', TagRetrieveAPIView.as_view()),

    path('news/', NewsAPIList.as_view()),
    path('news/<int:pk>', NewsAPIUpdate.as_view()),
    path('news/delete/<int:pk>', NewsAPIDestroy.as_view()),

]
