# -*- coding: utf-8 -*-
from django.urls import path
from website.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='inicio'),
]
