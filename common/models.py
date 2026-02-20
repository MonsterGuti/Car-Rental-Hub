from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    customer_name = models.CharField(
        max_length=100,
        help_text="Enter the name of the customer leaving the review."
    )

    content = models.TextField(
        help_text="Write the review content here."
    )

    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating must be between 1 and 5."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.customer_name} - {self.rating}/5"