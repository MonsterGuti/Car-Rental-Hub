from django.db import models
from django.utils import timezone


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    SEDAN = 'sedan'
    SUV = 'suv'
    HATCHBACK = 'hatchback'
    COUPE = 'coupe'
    CABRIOLET = 'cabriolet'
    MINIVAN = 'minivan'
    TRUCK = 'truck'

    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (HATCHBACK, 'Hatchback'),
        (COUPE, 'Coupe'),
        (CABRIOLET, 'Cabriolet'),
        (MINIVAN, 'Minivan'),
        (TRUCK, 'Truck'),
    ]

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    car_type = models.CharField(
        max_length=20,
        choices=CAR_TYPE_CHOICES,
        default=SEDAN,
        verbose_name='Type of Car',
        null=True,
        blank=True
    )
    year = models.PositiveIntegerField()
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.FileField(upload_to='car_images')
    is_available = models.BooleanField(default=True)
    features = models.ManyToManyField(Feature, blank=True)

    @property
    def is_available_now(self):
        today = timezone.localdate()

        return not self.rental_set.filter(
            start_date__lte=today,
            end_date__gte=today
        ).exists()

    def __str__(self):
        return f"{self.brand.name} {self.model} ({self.year})"
