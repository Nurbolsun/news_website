from django.urls import path

from account.views import UserAPIList

urlpatterns = [
    path('account/', UserAPIList.as_view()),
]
