from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_app.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput,
        label="email:"
        )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Пароль:"
        )


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
        ]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }
