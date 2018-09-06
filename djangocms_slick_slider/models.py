# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField
from jsonfield import JSONField


@python_2_unicode_compatible
class SlickSlider(CMSPlugin):
    """
    Main Plugin Model for the slider.
    """

    class Meta:
        verbose_name = _('slick slider')
        verbose_name_plural = _('slick sliders')

    title = models.CharField(
        verbose_name=_('slider title'),
        max_length=255,
        null=True, blank=True)

    settings = JSONField(
        verbose_name=_('slick settings'),
        blank=True, null=True,
        help_text=_(
            'Check <a href="http://kenwheeler.github.io/slick/" '
            'target="_blank">'
            'Slick Documentation</a> for possible settings '
            '<br>'
            'Use JSON format and check the errors in the editor<br>'
            'You can also use online JSON validators'))

    arrow_color = models.CharField(
        verbose_name=_('arrow color'),
        max_length=255,
        default="#666",
        help_text=_('Define the color of slider arrows here. All CSS '
                    'color values work (e.g. #efefef).'))

    def copy_relations(self, oldinstance):
        """
        Take an instance and copy the images of that instance to this
        instance.
        """
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
        ordering = ['position']

    slider = models.ForeignKey(
        SlickSlider,
        related_name="images")

    image = FilerImageField(
        verbose_name=_('slider Image'),
        related_name='slider_images_filer'
    )

    link = models.URLField(
        verbose_name=_('image link'),
        null=True, blank=True)

    caption_text = models.CharField(
        _('caption text'),
        max_length=255,
        null=True,
        blank=True)

    position = models.PositiveSmallIntegerField(
        verbose_name=_("Image order"),
        null=True,
        blank=True,
        default=0,
    )

    link_target = models.BooleanField(
        verbose_name=_('image link target'),
        help_text=_('open link in new window'),
        default=True)

    def __str__(self):
        """
        String representation of SlickSliderImage class.
        """
        return "{filename}".format(filename=self.image.original_filename)
