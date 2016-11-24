from django.db import models
from django.shortcuts import resolve_url


class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    website = models.URLField('Website', blank=True)
    slug = models.SlugField('Slug')
    photo = models.URLField('Foto')
    description = models.TextField('Descrição', blank=True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('speaker_detail', slug=self.slug )