from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.static import serve

from my_app.views import (
    NewsRetrieveAPIView, CategoryRetrieveAPIView,
    TagRetrieveAPIView, AllCategoryAPIView,
    AllNewsAPIView, MainAPIView, NewsDetailView
)
from turism.views import HomePageView

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', MainAPIView.as_view()),
    # path('news/<int:pk>', NewsRetrieveAPIView.as_view()),
    path('news/', AllNewsAPIView.as_view(), name='all-news'),
    path('category/', AllCategoryAPIView.as_view(), name='all-categories'),
    path('category/<int:pk>', CategoryRetrieveAPIView.as_view()),
    path('tag/<int:pk>', TagRetrieveAPIView.as_view()),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-detail'),
    path('post/', NewsRetrieveAPIView.as_view(), name='posts'),
    path('api/v1/', include('turism.urls')),

]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    urlpatterns += re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
