from django.urls import path, include

from .views import (
    HomePageView, RegionNameListView,
    RegionListView, RegionDetailView,
    CategoryListView, CategoryDetailView,
    PlacesByCategoryView,
    PlacesByRegionView, PlacesByMonthView,
    PLacesByTravellerView, PlaceListView,
    PlaceDetailView, MonthListView,
    TravellerListView, VideoView,
    CommentaryListView, FeedbackListCreateView
)


urlpatterns = [
    path('homepage/', HomePageView.as_view(), name='homepage'),
    path('video/', VideoView.as_view(), name='video'),
    path('regions_list/', RegionNameListView.as_view(), name='regions-list'),
    path('regions/', RegionListView.as_view(), name='regions'),
    path('regions/<int:pk>/', RegionDetailView.as_view(), name='regions-detail'),
    path('categories/', CategoryListView.as_view(), name='categories-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='categories-detail'),
    path('places/by_category/<int:category_id>/', PlacesByCategoryView.as_view(), name='places-by-category'),
    path('places/by_region/<int:region_id>/', PlacesByRegionView.as_view(), name='places-by-region'),
    path('places/by_month/<int:month_id>/', PlacesByMonthView.as_view(), name='places-by-month'),
    path('places/by_traveller/<int:traveller_id>/', PLacesByTravellerView.as_view(), name='places-by-traveller'),
    path('places/', PlaceListView.as_view(), name='places-list'),
    path('places/<int:pk>/', PlaceDetailView.as_view(), name='places-detail'),
    path('months/', MonthListView.as_view(), name='months-list'),
    path('travellers/', TravellerListView.as_view(), name='travellers-list'),
    path('commentary/', CommentaryListView.as_view(), name='commentary-list'),
    path('feedback/', FeedbackListCreateView.as_view(), name='feedback-list-create'),
]