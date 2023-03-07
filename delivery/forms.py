from django import forms
from django.contrib.auth.models import User
from django.forms import EmailInput, ModelForm, PasswordInput


class RegisterForm(ModelForm):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=PasswordInput)
    password2 = forms.CharField(widget=PasswordInput)
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=EmailInput
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]