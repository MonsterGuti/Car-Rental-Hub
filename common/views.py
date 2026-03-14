from datetime import date

from django.db.models import Count, Avg
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from django.shortcuts import redirect, get_object_or_404
from cars.models import Car
from common.models import Review
from common.forms import ReviewForm
from rentals.models import Rental


class HomeView(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_cars'] = Car.objects.order_by('-id')[:3]
        context['reviews'] = Review.objects.order_by('-created_at')[:3]
        return context


class AddReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'common/review-form.html'

    def get_initial(self):
        initial = super().get_initial()
        car_pk = self.kwargs.get('car_pk')
        if car_pk:
            initial['car'] = get_object_or_404(Car, pk=car_pk)
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        car_pk = self.kwargs.get('car_pk')
        if car_pk:
            form.fields['car'].disabled = True
        else:
            form.fields['car'].disabled = False
            form.fields['car'].queryset = Car.objects.all()
        return form

    def form_valid(self, form):
        car_pk = self.kwargs.get('car_pk')
        if car_pk:
            form.instance.car = get_object_or_404(Car, pk=car_pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('cars:car-detail', kwargs={'pk': self.object.car.pk})


class ReviewListView(ListView):
    model = Review
    template_name = 'common/review_list.html'
    context_object_name = 'reviews'
    ordering = ['-created_at']
    paginate_by = 6


class DashboardView(TemplateView):
    template_name = 'common/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_cars'] = Car.objects.count()
        context['available_cars'] = Car.objects.filter(is_available=True).count()
        context['active_rentals'] = Rental.objects.filter(end_date__gte=date.today()).count()
        context['average_rating'] = Review.objects.aggregate(Avg('rating'))['rating__avg'] or 0
        context['latest_rentals'] = Rental.objects.order_by('-id')[:5]
        context['latest_reviews'] = Review.objects.order_by('-id')[:5]
        context['car_names'] = list(Car.objects.values_list('model', flat=True))
        context['rentals_count'] = list(Car.objects.annotate(r_count=Count('rental')).values_list('r_count', flat=True))
        return context
