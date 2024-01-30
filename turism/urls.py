from django.urls import path, include

from .views import (
    HomePageView, RegionNameListView,
    RegionListView, RegionDetailView,
    CategoryListView,
    PlaceListView, PlaceDetailView,
    PlaceIncompleteListView
)


urlpatterns = [
    path('homepage/', HomePageView.as_view(), name='homepage'),
    path('regions_list/', RegionNameListView.as_view(), name='regions-list'),
    path('regions/', RegionListView.as_view(), name='regions'),
    path('regions/<int:pk>/', RegionDetailView.as_view(), name='regions-detail'),
    path('categories/', CategoryListView.as_view(), name='categories-list'),
    path('places/', PlaceListView.as_view(), name='places-list'),
    path('places/<int:pk>/', PlaceDetailView.as_view(), name='places=detail'),
    path('places-incomplete/', PlaceIncompleteListView.as_view(), name='places-incomplete')
]