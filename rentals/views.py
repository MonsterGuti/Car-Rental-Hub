from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cars.models import Car
from notifications.utils import create_notification_async
from rentals.models import Rental
from rentals.forms import RentalForm


class RentalListView(ListView):
    model = Rental
    template_name = 'rentals/rental_list.html'
    context_object_name = 'rentals'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        querydict = self.request.GET.copy()
        if 'page' in querydict:
            querydict.pop('page')
        context['querystring'] = querydict.urlencode()
        return context


class RentalDetailView(DetailView):
    model = Rental
    template_name = 'rentals/rental_detail.html'
    context_object_name = 'rental'


class RentalCreateView(LoginRequiredMixin, CreateView):
    model = Rental
    form_class = RentalForm
    template_name = 'rentals/rental_create.html'
    success_url = reverse_lazy('rentals:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        car_id = self.request.GET.get('car')
        if car_id:
            self.car_instance = get_object_or_404(Car, pk=car_id)
            kwargs['car_instance'] = self.car_instance
        return kwargs

    def form_valid(self, form):
        if not form.cleaned_data.get('car') and hasattr(self, 'car_instance'):
            form.instance.car = self.car_instance

        form.instance.user = self.request.user

        response = super().form_valid(form)

        print(f"ПРАЩАМ ИЗВЕСТИЕ ЗА: {self.request.user}")
        create_notification_async(
            self.request.user,
            f"Successfully rented {form.instance.car}. Dates: {form.instance.start_date} to {form.instance.end_date}"
        )
        return response

    def form_invalid(self, form):
        print("ГРЕШКИ ВЪВ ФОРМАТА:", form.errors)
        return super().form_invalid(form)


class RentalUpdateView(UpdateView):
    model = Rental
    form_class = RentalForm
    template_name = 'rentals/rental_update.html'
    success_url = reverse_lazy('rentals:list')


class RentalDeleteView(DeleteView):
    model = Rental
    template_name = 'rentals/rental_delete.html'
    success_url = reverse_lazy('rentals:list')
