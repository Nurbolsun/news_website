from django.views.generic import CreateView
from rest_framework import generics, status
from rest_framework.response import Response
from account.forms import UserRegisterForm
from account.models import CustomUser
from account.serializers import UserSerializers


class UserAPIList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers


class UserRegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
