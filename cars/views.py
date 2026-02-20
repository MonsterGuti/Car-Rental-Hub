from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Car
from .mixins import CarFilterMixin
from .forms import CarForm


class CarListView(CarFilterMixin, ListView):
    model = Car
    template_name = 'cars/car-list.html'
    context_object_name = 'cars'
    paginate_by = 6
    filter_available_only = False


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car-create.html'
    success_url = '/cars/'


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car-detail.html'
    context_object_name = 'car'


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car-update.html'

    def get_success_url(self):
        return reverse_lazy('cars:car-detail', kwargs={'pk': self.object.pk})


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('cars:car-list')
