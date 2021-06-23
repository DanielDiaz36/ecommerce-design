# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from core.models import DesignCategory


@admin.register(DesignCategory)
class DesignCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'slug',
    ]
    search_fields = [
        'name',
    ]
    list_filter = ['is_active']
    ordering = ['id']
    list_per_page = 20
