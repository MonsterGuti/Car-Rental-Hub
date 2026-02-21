from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from rentals.models import Rental
from rentals.forms import RentalForm


class RentalListView(ListView):
    model = Rental
    template_name = 'rentals/rental_list.html'
    context_object_name = 'rentals'
    paginate_by = 3


class RentalDetailView(DetailView):
    model = Rental
    template_name = 'rentals/rental_detail.html'
    context_object_name = 'rental'


class RentalCreateView(CreateView):
    model = Rental
    form_class = RentalForm
    template_name = 'rentals/rental_create.html'
    success_url = reverse_lazy('rentals:list')


class RentalUpdateView(UpdateView):
    model = Rental
    form_class = RentalForm
    template_name = 'rentals/rental_update.html'
    success_url = reverse_lazy('rentals:list')


class RentalDeleteView(DeleteView):
    model = Rental
    template_name = 'rentals/rental_delete.html'
    success_url = reverse_lazy('rentals:list')
