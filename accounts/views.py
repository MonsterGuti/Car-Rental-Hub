from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from .forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class AppLoginView(LoginView):
    template_name = 'accounts/login.html'


class AppLogoutView(LogoutView):
    next_page = reverse_lazy('login')
