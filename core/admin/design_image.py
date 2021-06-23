# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from core.models import DesignImage


@admin.register(DesignImage)
class DesignImageAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'design',
        'image',
        'is_main_image'
    ]
    search_fields = [
        'design',
        'is_main_image'
    ]
    list_filter = ['is_active']
    ordering = ['id']
    list_per_page = 20
