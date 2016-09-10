from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        self.data = dict(name="Fernando Silva", cpf="12345678901",
                         email="qwe@qwe.com", phone="23-2323-2323")
        self.response = self.client.post('/inscricao/', self.data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com', 'qwe@qwe.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Fernando Silva',
            '12345678901',
            'qwe@qwe.com',
            '23-2323-2323',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
