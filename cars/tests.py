from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from model_bakery import baker
from django.core.files.uploadedfile import SimpleUploadedFile
from cars.models import Car, Brand

User = get_user_model()

class CarTests(TestCase):
    def setUp(self):
        self.user = baker.make(User)
        self.brand = baker.make(Brand, name='Tesla')
        self.img = SimpleUploadedFile('car.jpg', b'')
        self.car = baker.make(Car, brand=self.brand, owner=self.user, price_per_day=100, image=self.img)

    def test_car_str_method(self):
        self.assertIn('Tesla', str(self.car))

    def test_car_list_view_status(self):
        response = self.client.get(reverse('cars:car-list'))
        self.assertEqual(response.status_code, 200)

    def test_car_detail_view_status(self):
        response = self.client.get(reverse('cars:car-detail', kwargs={'pk': self.car.pk}))
        self.assertEqual(response.status_code, 200)

    def test_unauthorized_car_delete(self):
        other_user = baker.make(User)
        self.client.force_login(other_user)
        url = reverse('cars:car-delete', kwargs={'pk': self.car.pk})
        response = self.client.post(url)
        self.assertIn(response.status_code, [403, 302])

    def test_api_car_list_accessible(self):
        response = self.client.get(reverse('cars:api-car-list'))
        self.assertEqual(response.status_code, 200)

    def test_car_availability_toggle(self):
        self.car.is_available = False
        self.car.save()
        self.assertFalse(Car.objects.get(pk=self.car.pk).is_available)