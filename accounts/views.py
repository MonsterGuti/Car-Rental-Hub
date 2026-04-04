from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('common:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class AppLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('cars:car-list')


class AppLogoutView(LogoutView):
    success_url = reverse_lazy('accounts:login')
