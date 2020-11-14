# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserCategory(models.Model):

    name = models.CharField(verbose_name=_('nombre'), max_length=50)

    description = models.CharField(verbose_name=_('descripción'), max_length=250, blank=True, null=True)

    created_at = models.DateTimeField(verbose_name=_('fecha de creado'), auto_now_add=True)

    updated_at = models.DateTimeField(verbose_name=_('fecha de actualización'), auto_now=True)

    deleted_at = models.DateTimeField(verbose_name=_('fecha de eliminación'), blank=True, null=True)

    is_active = models.BooleanField(verbose_name=_('activo'), default=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'core'
        db_table = 'core_user_category'
        verbose_name = _('categoría de usuario')
        verbose_name_plural = _('categorías de usuario')
        ordering = ['id']
