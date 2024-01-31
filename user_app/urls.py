from django.urls import path, include
from user_app import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.user_logout, name="logout"),
]