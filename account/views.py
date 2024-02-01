from rest_framework import generics

from account.models import User
from account.serializers import UserSerializers


class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
