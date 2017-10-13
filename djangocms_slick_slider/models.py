# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, connection
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField
from adminsortable.models import Sortable

from .settings import get_setting

if 'postgre' in connection.vendor:
    from django.contrib.postgres.fields import JSONField
else:
    try:
        from jsonfield import JSONField
    except ImportError:
        raise Exception('You need to have "jsonfield" installed: pip install '
                        'jsonfield')


@python_2_unicode_compatible
class SlickSlider(CMSPlugin):
    """
    Main Plugin Model for the slider.
    """
    title = models.CharField(
        verbose_name=_('slider title'),
        max_length=255)

    settings = JSONField(
        verbose_name=_('slick settings'),
        default=get_setting('SLICK_SLICKER_DEFAULT_OPTIONS'))

    arrow_color = models.CharField(
        verbose_name=_('arrow color'),
        max_length=255,
        default="#ddd",
        help_text=_('Define the color of slider arrows here. All CSS '
                    'color values work (e.g. #efefef)'))

    def copy_relations(self, oldinstance):
        for image in oldinstance.images.all():
            image.pk = None
            image.slider = self
            image.save()

    def __str__(self):
        """
        String representation of SlickSlider class.
        """
        return "{title}".format(title=self.title)


@python_2_unicode_compatible
class SlickSliderImage(models.Model):
    """
    Image model für SlickSlider class.
    """
    class Meta:
        verbose_name = _('slider image')
        verbose_name_plural = _('slider images')

    slider = models.ForeignKey(
        SlickSlider,
        related_name="images"
    )

    image = FilerImageField(
        verbose_name=_('slider Image'),
        related_name='slider_images_filer')

    link = models.URLField(
        verbose_name=_('image link'),
        null=True, blank=True)

    caption_text = models.TextField(
        _('caption text'),
        null=True,
        blank=True,
    )

    def __str__(self):
        """
        String representation of SlickSliderImage class.
        """
        if self.caption_text:
            return self.caption_text
        if self.image.label:
            return self.image.label
        else:
            return "{filename}".format(
                filename=self.image.original_filename)
