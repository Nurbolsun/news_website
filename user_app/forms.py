from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput,
        label="email:"
        )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Пароль:"
        )