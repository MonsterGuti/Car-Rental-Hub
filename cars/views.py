from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from cars.models import Car, Brand, Feature
from cars.mixins import CarFilterMixin
from cars.forms import CarForm, CarDeleteForm, BrandForm, FeatureForm
from notifications.utils import create_notification_async


class CarListView(CarFilterMixin, ListView):
    model = Car
    template_name = 'cars/car-list.html'
    context_object_name = 'cars'
    paginate_by = 3
    filter_available_only = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        querydict = self.request.GET.copy()
        if 'page' in querydict:
            querydict.pop('page')
        context['querystring'] = querydict.urlencode()
        return context


class CarCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car-create.html'
    success_url = '/cars/'
    permission_required = 'cars.add_car'
    raise_exception = True

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)

        create_notification_async(
            self.request.user,
            f"You created car {form.instance}"
        )

        return response


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
        context['image_url'] = car.image.url if car.image else None
        context['availability'] = "Available" if car.is_available else "Not Available"
        context['availability_class'] = "bg-success" if car.is_available else "bg-secondary"

        features = car.features.all()
        context['features_list'] = ", ".join([f.name for f in features]) if features else "None"

        if reviews.exists():
            average = sum(r.rating for r in reviews) / reviews.count()
            context['average_rating'] = round(average, 1)
        else:
            context['average_rating'] = None

        return context


class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car-update.html'

    def test_func(self):
        car = self.get_object()
        return car.owner == self.request.user or self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy('cars:car-detail', kwargs={'pk': self.object.pk})


class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('cars:car-list')

    def test_func(self):
        car = self.get_object()
        return car.owner == self.request.user or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CarDeleteForm(instance=self.object)
        return context


class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'cars/brand_create.html'
    success_url = reverse_lazy('cars:car-list')
    permission_required = 'cars.add_brand'
    raise_exception = True


class BrandListView(ListView):
    model = Brand
    template_name = 'cars/brand_list.html'
    context_object_name = 'brands'


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'cars/brand_detail.html'
    context_object_name = 'brand'


class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'cars/brand_update.html'
    success_url = reverse_lazy('cars:brand-list')
    permission_required = 'cars.change_brand'
    raise_exception = True


class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Brand
    template_name = 'cars/brand_delete.html'
    success_url = reverse_lazy('cars:brand-list')
    permission_required = 'cars.delete_brand'
    raise_exception = True


class FeatureCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Feature
    form_class = FeatureForm
    template_name = 'cars/feature_create.html'
    success_url = reverse_lazy('cars:car-list')
    permission_required = 'cars.add_feature'
    raise_exception = True


class FeatureListView(ListView):
    model = Feature
    template_name = 'cars/feature_list.html'
    context_object_name = 'features'


class FeatureDetailView(DetailView):
    model = Feature
    template_name = 'cars/feature_detail.html'
    context_object_name = 'feature'


class FeatureUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Feature
    form_class = FeatureForm
    template_name = 'cars/feature_update.html'
    success_url = reverse_lazy('cars:feature-list')
    permission_required = 'cars.change_feature'
    raise_exception = True


class FeatureDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Feature
    template_name = 'cars/feature_delete.html'
    success_url = reverse_lazy('cars:feature-list')
    permission_required = 'cars.delete_feature'
    raise_exception = True
