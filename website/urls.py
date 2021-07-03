# -*- coding: utf-8 -*-
from website import views
from django.urls import path
from django.utils.translation import gettext_lazy as _


urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),

    path(_('portfolio'), views.PortfolioView.as_view(), name='portfolio'),

    path(_('diseños'), views.DesignsView.as_view(), name='designs'),

    path(_('servicios'), views.ServicesView.as_view(), name='services'),

    path(_('precios'), views.PricingView.as_view(), name='pricing'),

    path(_('blog'), views.BlogView.as_view(), name='blog'),

    path(_('contacto'), views.ContactView.as_view(), name='contact'),

    path(_('podcast'), views.PodcastView.as_view(), name='podcast'),

    path(_('sobre-nosotros'), views.AboutView.as_view(), name='about'),

    path(_('preguntas-frecuentes'), views.FAQView.as_view(), name='faq'),

    path(_('politica-de-privacidad'), views.PolicyView.as_view(), name='policy'),

    path(_('politica-de-cancelacion-y-devolucion'), views.CancelPolicyView.as_view(), name='cancel_policy'),

    path(_('terminos-y-condiciones'), views.TermsView.as_view(), name='terms'),

]
