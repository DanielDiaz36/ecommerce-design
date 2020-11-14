# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytz
from django.utils import timezone, formats


def convert_to_localtime(utctime):
    utc = utctime.replace(tzinfo=pytz.UTC)
    localtz = utc.astimezone(timezone.get_current_timezone())

    return formats.date_format(localtz, 'DATETIME_FORMAT')
