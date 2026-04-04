from django.test import TestCase
from datetime import date, timedelta
from model_bakery import baker
from rentals.models import Rental
from rentals.forms import RentalForm
from cars.models import Car


class RentalTests(TestCase):
    def setUp(self):
        self.car = baker.make(Car, price_per_day=50.0)

    def test_total_price_calculation(self):
        start = date.today()
        end = start + timedelta(days=2)
        rental = baker.make(Rental, car=self.car, start_date=start, end_date=end)

        self.assertEqual(float(rental.total_price), 150.0)

    def test_rental_form_valid_data(self):
        form_data = {
            'car': self.car.id,
            'customer_name': 'Ivan',
            'customer_email': 'ivan@test.com',
            'start_date': date.today(),
            'end_date': date.today() + timedelta(days=1)
        }
        form = RentalForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_email_in_rental_form(self):
        form_data = {
            'car': self.car.id,
            'customer_email': 'softuni-mail.com',
            'customer_name': 'Ivan',
            'start_date': date.today(),
            'end_date': date.today() + timedelta(days=1)
        }
        form = RentalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_rental_deletion(self):
        rental = baker.make(Rental)
        rental_id = rental.id
        rental.delete()
        self.assertFalse(Rental.objects.filter(id=rental_id).exists())
