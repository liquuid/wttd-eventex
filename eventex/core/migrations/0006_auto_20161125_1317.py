# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-25 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_talk'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='speakers',
            field=models.ManyToManyField(to='core.Speaker'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='start',
            field=models.TimeField(null=True),
        ),
    ]
