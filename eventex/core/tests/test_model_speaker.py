from django.shortcuts import resolve_url
from django.test import TestCase
from eventex.core.models import Speaker


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            website='http://hbn.link/hopper-site',
            photo='http://hbn.link/hopper-pic',
            description='Programadora e almirante.<br/> \
                Inventora do compilador, criadora da linguagem de programação\
                Flow-Matic servido de vase para a linguagem COBOL permitindo\
                a popularização das aplicações comerciais.',
        )

    def test_create(self):
        self.assertTrue(Speaker.objects.exists())

    def test_description_can_be_blank(self):
        field = Speaker._meta.get_field('description')
        self.assertTrue(field.blank)


    def test_website_can_be_blank(self):
        field = Speaker._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_str(self):
        self.assertEqual('Grace Hopper', str(self.speaker))

    def test_get_absolute_url(self):
        url = resolve_url('speaker_detail', slug=self.speaker.slug)
        self.assertEqual(url, self.speaker.get_absolute_url())