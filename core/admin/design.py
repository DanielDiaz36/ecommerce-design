# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from core.models import Design


@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'description',
        'link_demo',
    ]
    search_fields = [
        'name',
        'description',
        'link_demo',
        'category'
    ]
    list_filter = ['is_active']
    ordering = ['id']
    list_per_page = 20
