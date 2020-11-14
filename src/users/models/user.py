# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.utils.date import convert_to_localtime
from core.models.user_category import UserCategory
from core.models.country import Country


class User(AbstractUser):

    first_name = models.CharField(verbose_name=_('nombre'), max_length=100)

    last_name = models.CharField(verbose_name=_('apellidos'), max_length=200)

    email = models.EmailField(verbose_name=_('email'), unique=True)

    is_staff = models.BooleanField(_('staff'), default=False)

    is_active = models.BooleanField(_('activo'), default=False)

    is_superuser = models.BooleanField(_('superuser status'), default=False)

    # Extras:

    company = models.CharField(verbose_name=_('compañía'), max_length=50, blank=True, null=True)

    user_category = models.ForeignKey(UserCategory, verbose_name=_('categoría de usuario'), on_delete=models.PROTECT)

    city = models.CharField(max_length=50, verbose_name=_('ciudad'), blank=True, null=True)

    country = models.ForeignKey(Country, verbose_name=_('país'), on_delete=models.PROTECT, blank=True, null=True)

    phone_prefix = models.CharField(max_length=4, blank=True, null=True)

    phone = models.CharField(verbose_name=_('teléfono'), max_length=15, blank=True, null=True)

    facebook = models.CharField(verbose_name=_('facebook'), max_length=50, blank=True, null=True)

    whatsapp = models.CharField(verbose_name=_('whatsapp'), max_length=50, blank=True, null=True)

    updated_at = models.DateTimeField(verbose_name=_('fecha de actualización'), auto_now=True)

    activated_at = models.DateTimeField(verbose_name=_('fecha de activación'), blank=True, null=True)

    password_changed_at = models.DateTimeField(verbose_name=_('fecha de cambio de contraseña'), blank=True, null=True)

    deleted_at = models.DateTimeField(verbose_name=_('fecha de eliminación'), blank=True, null=True)

    is_deleted = models.BooleanField(verbose_name=_('eliminiado'), default=False)

    locked_at = models.DateTimeField(verbose_name=_('fecha de deshabilitación'), blank=True, null=True)

    def __str__(self):
        return self.first_name

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def phone_number(self):
        return "(+" + self.phone_prefix + ") " + self.phone if self.phone_prefix and self.phone else None

    def is_activated_at(self):
        return convert_to_localtime(self.activated_at) if self.pk is not None and self.is_active else ' - '

    def is_locked_at(self):
        return convert_to_localtime(self.locked_at) if self.pk is not None and self.is_active is False else ' - '

    def get_email(self):
        return self.email.encode('utf-8')

    def get_country_code(self):
        return self.country.code

    fullname.short_description = _('Nombre y apellidos')
    is_activated_at.short_description = _('Activado en')
    is_locked_at.short_description = _('Bloqueado en')
    phone_number.short_description = _('Teléfono')

    class Meta:
        app_label = 'users'
        db_table = 'auth_user'
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')
