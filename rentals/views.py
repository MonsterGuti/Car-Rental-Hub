from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from rentals.mixins import RentalMixin
from rentals.models import Rental


class RentalListView(ListView):
    model = Rental
    template_name = 'rentals/rental_list.html'
    context_object_name = 'rentals'
    paginate_by = 3


class RentalDetailView(DetailView):
    model = Rental
    template_name = 'rentals/rental_detail.html'
    context_object_name = 'rental'


class RentalCreateView(RentalMixin, CreateView):
    template_name = 'rentals/rental_create.html'

    def get_initial(self):
        initial = super().get_initial()
        car_id = self.request.GET.get('car')
        if car_id:
            initial['car_id'] = car_id
        return initial


class RentalUpdateView(RentalMixin, UpdateView):
    template_name = 'rentals/rental_update.html'


class RentalDeleteView(RentalMixin, UpdateView):
    template_name = 'rentals/rental_delete.html'


