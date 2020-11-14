# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

register = template.Library()


def remplace_space(value):
    return value.replace(" ", "-")


register.filter('remplace_space', remplace_space)
