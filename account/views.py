from django.contrib.auth.tokens import default_token_generator
from django.views.generic import CreateView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from account.forms import UserRegisterForm
from account.models import CustomUser
from account.serializers import UserSerializers
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode


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


class PasswordResetConfirmAPIView(APIView):
    def post(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        new_password = request.data.get('new_password')
        try:
            uuid = force_str(urlsafe_base64_encode(uidb64))
            user = CustomUser.objects.get(pk=uuid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.set_password(new_password)
            user.save()
            return Response({'detail': 'Password reset successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid token or user'}, status=status.HTTP_400_BAD_REQUEST)