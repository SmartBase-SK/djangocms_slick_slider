# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-19 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlickSlider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_slick_slider_slickslider', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, verbose_name='slider title')),
                ('settings', jsonfield.fields.JSONField(default=b'{\n    "autoplay": true, \n    "autoplaySpeed": 1200, \n    "dots": true, \n    "mobileFirst": false, \n    "slidesToScroll": 4, \n    "slidesToShow": 4\n}', verbose_name='slick settings')),
                ('arrow_color', models.CharField(default='#ddd', help_text='Define the color of slider arrows here. All CSS color values work (e.g. #efefef)', max_length=255, verbose_name='arrow color')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SlickSliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, null=True, verbose_name='image link')),
                ('caption_text', models.TextField(blank=True, null=True, verbose_name='caption text')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='slider_images_filer', to='filer.Image', verbose_name='slider Image')),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='djangocms_slick_slider.SlickSlider')),
            ],
            options={
                'verbose_name': 'slider image',
                'verbose_name_plural': 'slider images',
            },
        ),
    ]
