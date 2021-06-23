# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from core.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'code',
    ]
    search_fields = [
        'name',
        'code',
    ]
    list_filter = ['is_active']
    ordering = ['id']
    list_per_page = 20
