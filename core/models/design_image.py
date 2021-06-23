# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.models.design import Design


class DesignImage(models.Model):

    design = models.ForeignKey(Design, on_delete=models.PROTECT)

    image = models.ImageField(upload_to='design_image/')

    is_main_image = models.BooleanField(verbose_name=_('imagen principal'), default=True)

    created_at = models.DateTimeField(verbose_name=_('fecha de creado'), auto_now_add=True)

    updated_at = models.DateTimeField(verbose_name=_('fecha de actualización'), auto_now=True)

    deleted_at = models.DateTimeField(verbose_name=_('fecha de eliminación'), blank=True, null=True)

    is_active = models.BooleanField(verbose_name=_('activo'), default=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_design_image'
        verbose_name = _('imagen de diseño')
        verbose_name_plural = _('imágenes de diseño')
        ordering = ['id']