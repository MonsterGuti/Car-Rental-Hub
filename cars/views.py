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

    def get_queryset(self):
        return Car.objects.select_related('brand').prefetch_related('features')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        reviews = car.reviews.all()

        context['reviews'] = reviews
        context['brand_name'] = car.brand.name
        context['model_name'] = car.model
        context['car_year'] = car.year
        context['price'] = car.price_per_day
        context['image_url'] = car.image
        context['availability'] = "Available" if car.is_available else "Not Available"
        context['availability_class'] = "bg-success" if car.is_available else "bg-secondary"
        context['reviews'] = car.reviews.all()

        features = car.features.all()
        context['features_list'] = ", ".join([f.name for f in features]) if features else "None"

        if reviews.exists():
            average = sum(r.rating for r in reviews) / reviews.count()
            context['average_rating'] = round(average, 1)
        else:
            context['average_rating'] = None

        return context


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
