from django.views.generic import FormView, CreateView, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from user_app.models import  User
from user_app.forms import LoginForm, UserRegisterForm
from django.urls import reverse_lazy


# Create your views here.


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        email = data["email"]
        password = data["password"]
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect("../../admin/")
            else:
                HttpResponse("Ваш аккаунт не актвен")
        HttpResponse("Такого пользвателя не существует")


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("all")


class UserRegisterView(CreateView):
    model = User
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("register_done")


class RegisterDoneView(TemplateView):
    template_name = "register_done.html"


