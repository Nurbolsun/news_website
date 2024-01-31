from django.urls import path, include
from user_app import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("register/done/", views.RegisterDoneView.as_view(), name="register_done"),
]