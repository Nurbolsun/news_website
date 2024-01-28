"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app.views import NewsRetrieveAPIView, CategoryRetrieveAPIView, TagRetrieveAPIView, AllCategoryAPIView,\
    AllNewsAPIView, MainAPIView, NewsDetailView
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Post API",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainAPIView.as_view()),
    # path('news/<int:pk>', NewsRetrieveAPIView.as_view()),
    path('news/', AllNewsAPIView.as_view(), name='all-news'),
    path('category/', AllCategoryAPIView.as_view(), name='all-categories'),
    path('category/<int:pk>', CategoryRetrieveAPIView.as_view()),
    path('tag/<int:pk>', TagRetrieveAPIView.as_view()),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-detail'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('post/', NewsRetrieveAPIView.as_view(), name='posts'),


]
