from django.views.generic import TemplateView, CreateView
from django.shortcuts import redirect, get_object_or_404
from cars.models import Car
from common.models import Review
from common.forms import ReviewForm


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

    def dispatch(self, request, *args, **kwargs):
        self.car = get_object_or_404(Car, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        review = form.save(commit=False)
        review.car = self.car
        review.save()
        return redirect('cars:car-detail', pk=self.car.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = self.car
        return context