# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-06 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_slick_slider', '0005_auto_20180906_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slicksliderimage',
            name='caption_text',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='caption text'),
        ),
        migrations.AlterField(
            model_name='slicksliderimage',
            name='position',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Image order'),
        ),
    ]
