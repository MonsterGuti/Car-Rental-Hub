from django.db import models
from cars.models import Car
from django.core.exceptions import ValidationError
from datetime import date

class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date must be after start date.")
        if self.start_date < date.today():
            raise ValidationError("Start date cannot be in the past.")

    def save(self, *args, **kwargs):
        days = (self.end_date - self.start_date).days + 1
        self.total_price = days * self.car.price_per_day
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Rental: {self.car} for {self.customer_name}"