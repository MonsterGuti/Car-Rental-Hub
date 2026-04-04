from django.test import TestCase
from django.contrib.auth import get_user_model
from model_bakery import baker
from common.models import Review

User = get_user_model()


class CommonTests(TestCase):
    def setUp(self):
        self.car = baker.make('cars.Car')
        self.user = baker.make(User)

    def test_review_creation(self):
        review = baker.make(
            Review,
            car=self.car,
            user=self.user,
            rating=5,
            customer_name="Pesho"
        )
        self.assertEqual(review.rating, 5)

    def test_review_str_method(self):
        review = baker.make(
            Review,
            user=self.user,
            customer_name="Mariya",
            rating=4
        )
        self.assertEqual(str(review), "Mariya - 4/5")
