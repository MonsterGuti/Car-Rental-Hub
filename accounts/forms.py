from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import AppUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ['username', 'email', 'phone_number', 'profile_picture', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone number'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))