from django.shortcuts import render, redirect
from cars.models import Car
from .models import Review
from .forms import ReviewForm

def home_view(request):
    latest_cars = Car.objects.order_by('-id')[:3]
    reviews = Review.objects.order_by('-created_at')[:3]

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForm()

    context = {
        'latest_cars': latest_cars,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'common/home.html', context)


from django.shortcuts import render, redirect
from .forms import ReviewForm


def review_create_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car-list')  # или друга подходяща страница
    else:
        form = ReviewForm()

    return render(request, 'common/review-form.html', {'form': form})