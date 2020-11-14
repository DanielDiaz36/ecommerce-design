# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DesignCategory(models.Model):

    name = models.CharField(verbose_name=_('categoría'), max_length=100, unique=True)

    slug = models.SlugField(verbose_name=_('slug'), max_length=100, unique=True)

    created_at = models.DateTimeField(verbose_name=_('fecha de creado'), auto_now_add=True)

    updated_at = models.DateTimeField(verbose_name=_('fecha de actualización'), auto_now=True)

    deleted_at = models.DateTimeField(verbose_name=_('fecha de eliminación'), blank=True, null=True)

    is_active = models.BooleanField(verbose_name=_('activo'), default=True)

    def __str__(self):
        return self.name

    def child_designs(self):
        return self.design_set.filter(is_active=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_designcategory'
        verbose_name = _('categoría de diseño')
        verbose_name_plural = _('categorías de diseño')
        ordering = ['name']


class Design(models.Model):

    name = models.CharField(verbose_name=_('nombre'), max_length=100)

    description = models.CharField(verbose_name=_('descripción'), max_length=255, blank=False, null=False)

    link_demo = models.URLField(verbose_name=_('demo url'), max_length=255, blank=True, null=True)

    category = models.ManyToManyField(DesignCategory, verbose_name=_('categoría'))

    created_at = models.DateTimeField(verbose_name=_('fecha de creado'), auto_now_add=True)

    updated_at = models.DateTimeField(verbose_name=_('fecha de actualización'), auto_now=True)

    deleted_at = models.DateTimeField(verbose_name=_('fecha de eliminación'), blank=True, null=True)

    is_active = models.BooleanField(verbose_name=_('activo'), default=True)

    def __str__(self):
        return self.name

    def get_main_image(self):
        from .design_image import DesignImage
        images = DesignImage.objects.filter(design=self, is_main_image=True)
        if images.exists():
            return images[0]
        return None

    # def main_image(self):
    #     try:
    #         return mark_safe('<img src="{url}" width="{width}" height={height} alt="{name}"/>'.format(
    #             url=self.get_main_image().url,
    #             width=self.get_main_image().width,
    #             height=self.get_main_image().height,
    #             name=self.name
    #         ))
    #     except (FileNotFoundError, TypeError):
    #         return ' - '

    def get_all_images(self):
        from .design_image import DesignImage
        images = DesignImage.objects.filter(design=self, is_main_image=False)
        return images

    class Meta:
        app_label = 'core'
        db_table = 'core_design'
        verbose_name = _('diseño')
        verbose_name_plural = _('diseños')
        ordering = ['id']