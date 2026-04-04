from django.test import TestCase
from django.contrib.auth import get_user_model
from model_bakery import baker
from notifications.models import Notification

User = get_user_model()

class AccountsTests(TestCase):
    def setUp(self):
        self.user = baker.make(User, username='test_user', phone_number='0888123456')

    def test_user_creation_and_str(self):
        self.assertEqual(str(self.user), 'test_user')

    def test_unread_notifications_count(self):
        baker.make(Notification, user=self.user, is_read=False)
        self.assertEqual(self.user.unread_notifications_count, 1)

    def test_user_is_not_staff_by_default(self):
        self.assertFalse(self.user.is_staff)

    def test_profile_update_phone_number(self):
        self.user.phone_number = '0999999999'
        self.user.save()
        self.assertEqual(User.objects.get(pk=self.user.pk).phone_number, '0999999999')