from django.urls import reverse_lazy

from rentals.forms import RentalForm
from rentals.models import Rental


class RentalMixin:
    model = Rental
    form_class = RentalForm
    success_url = reverse_lazy('rentals:list')