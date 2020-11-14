# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from core.models import UserCategory


@admin.register(UserCategory)
class UserCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'description',
    ]
    search_fields = [
        'name',
        'description',
    ]
    list_filter = ['is_active']
    ordering = ['id']
    list_per_page = 20
