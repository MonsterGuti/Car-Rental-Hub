from django.db import models


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
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.URLField()
    is_available = models.BooleanField(default=True)
    features = models.ManyToManyField(Feature, blank=True)

    def __str__(self):
        return f"{self.brand.name} {self.model} ({self.year})"
