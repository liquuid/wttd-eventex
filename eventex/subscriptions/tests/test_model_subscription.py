from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj= Subscription(
            name='Name Surname',
            cpf='1234567890-1',
            email='qwe@qwe.net',
            phone='1212121212',
            paid=False,

        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto create_ad attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Name Surname', str(self.obj))

    def test_paid_default_to_false(self):
        """ By default paid must be false """
        self.assertEqual(False, self.obj.paid)