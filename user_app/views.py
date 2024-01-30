from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from user_app.forms import LoginForm


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
                return redirect("all")
            else:
                HttpResponse("Ваш аккаунт не актвен")
        HttpResponse("Такого пользвателя не существует")