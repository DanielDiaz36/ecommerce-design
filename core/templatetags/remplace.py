# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

register = template.Library()


@register.filter
def remplace_space(value):
    return value.replace(" ", "-")
