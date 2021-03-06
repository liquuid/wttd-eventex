from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accept digits"""
        form = self.make_validated_form(cpf='A2345678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def test_cpf_has_11_digits(self):
        """ CPF must have 11 digits"""
        form = self.make_validated_form(cpf='123')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_email_is_optional(self):
        """ Email is optional"""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """ Phone is optional"""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_phone_or_mail(self):
        """ Must inform phone or mail"""
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))


    def test_name_must_be_capitalized(self):
        """ Name must be capitalized"""
        form = self.make_validated_form(name="FERNANDO silva")
        self.assertEqual('Fernando Silva', form.cleaned_data['name'])

    def make_validated_form(self, **kwargs):
        valid = dict(name="Fernando Silva", cpf="12345678901",
                     email="qwe@qwe.com", phone="23-2323-2323")

        data = dict(valid, **kwargs)

        form = SubscriptionForm(data)
        form.is_valid()

        return form
