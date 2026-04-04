from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from model_bakery import baker
from notifications.models import Notification

User = get_user_model()

class NotificationTests(TestCase):
    def setUp(self):
        self.user = baker.make(User)
        self.notif = baker.make(Notification, user=self.user, is_read=False, message="Hello")

    def test_notification_str(self):
        self.assertEqual(str(self.notif), "Hello")

    def test_mark_as_read_on_visit(self): # Тест 15
        self.client.force_login(self.user)
        url = reverse('notifications')
        self.client.get(url)
        self.notif.refresh_from_db()
        self.assertTrue(self.notif.is_read)