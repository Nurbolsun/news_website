from django.urls import path
from account.views import UserAPIList, UserRegisterView

urlpatterns = [
    path('api/user/', UserAPIList.as_view()),
    path('api/user/<int:pk>', UserAPIList.as_view()),
    path('register/', UserRegisterView.as_view())
]
