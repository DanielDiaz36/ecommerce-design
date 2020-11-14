# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):

    name = models.CharField(verbose_name=_('nombre'), max_length=50, blank=False, null=False, unique=True)

    code = models.SlugField(verbose_name=_('código'), max_length=50, blank=False, null=False, unique=True)

    created_at = models.DateTimeField(verbose_name=_('fecha de creado'), auto_now_add=True)

    updated_at = models.DateTimeField(verbose_name=_('fecha de actualización'), auto_now=True)

    deleted_at = models.DateTimeField(verbose_name=_('fecha de eliminación'), blank=True, null=True)

    is_active = models.BooleanField(verbose_name=_('activo'), default=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'core'
        db_table = 'core_country'
        verbose_name = _('país')
        verbose_name_plural = _('países')
        ordering = ['name']
