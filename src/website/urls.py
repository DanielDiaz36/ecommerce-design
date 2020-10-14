# -*- coding: utf-8 -*-
from django.urls import path
from django.utils.translation import gettext_lazy as _

from website.views import (
    HomeView,
    DesignsView,
    ServicesView,
    PricingView,
    BlogView,
    PodcastView,
    ContactView,
    AboutView,
    PolicyView,
    TermsView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path(_('diseños'), DesignsView.as_view(), name='designs'),
    path(_('servicios'), ServicesView.as_view(), name='services'),
    path(_('precios'), PricingView.as_view(), name='pricing'),
    path(_('blog'), BlogView.as_view(), name='blog'),
    path(_('contacto'), ContactView.as_view(), name='contact'),
    path(_('podcast'), PodcastView.as_view(), name='podcast'),
    path(_('sobre-nosotros'), AboutView.as_view(), name='about'),
    path(_('politica-de-privacidad'), PolicyView.as_view(), name='policy'),
    path(_('terminos-y-condiciones'), TermsView.as_view(), name='terms'),
]
