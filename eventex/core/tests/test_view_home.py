from django.shortcuts import resolve_url
from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(resolve_url('home'))

    def test_get(self):
        """
        GET / must return status code 200
        """

        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        """Must use index.html """

        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(resolve_url('subscriptions:new'))
        self.assertContains(self.response, expected)