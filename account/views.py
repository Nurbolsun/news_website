from django.views.generic import CreateView
from rest_framework import generics, status
from rest_framework.response import Response
from account.forms import UserRegisterForm
from account.models import CustomUser
from account.serializers import UserSerializers


class UserAPIList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        if pk:
            user = self.get_object()
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        return self.list(request, *args, **kwargs)


class UserRegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
