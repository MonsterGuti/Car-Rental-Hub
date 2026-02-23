from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cars.models import Car
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


class RentalCreateView(CreateView):
    model = Rental
    form_class = RentalForm
    template_name = 'rentals/rental_create.html'
    success_url = reverse_lazy('rentals:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        car_id = self.request.GET.get('car')
        if car_id:
            car_instance = Car.objects.get(pk=car_id)
            kwargs['car_instance'] = car_instance
        return kwargs


class RentalUpdateView(UpdateView):
    model = Rental
    form_class = RentalForm
    template_name = 'rentals/rental_update.html'
    success_url = reverse_lazy('rentals:list')


class RentalDeleteView(DeleteView):
    model = Rental
    template_name = 'rentals/rental_delete.html'
    success_url = reverse_lazy('rentals:list')
