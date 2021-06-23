# -*- coding: utf-8 -*-
from django.utils.text import slugify
from django.views.generic import TemplateView

from core.models import Design, DesignCategory


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        ctx['inicio_active'] = True
        return ctx


class DesignsView(TemplateView):
    template_name = 'pages/designs.html'

    def get_context_data(self, **kwargs):
        ctx = super(DesignsView, self).get_context_data(**kwargs)
        ctx['designs_active'] = True
        ctx['designs'] = Design.objects.filter(is_active=True)
        ctx['designs_category'] = DesignCategory.objects.filter(is_active=True)
        return ctx


class ServicesView(TemplateView):
    template_name = 'pages/services.html'

    def get_context_data(self, **kwargs):
        ctx = super(ServicesView, self).get_context_data(**kwargs)
        ctx['services_active'] = True
        return ctx


class PricingView(TemplateView):
    template_name = 'pages/pricing.html'

    def get_context_data(self, **kwargs):
        ctx = super(PricingView, self).get_context_data(**kwargs)
        ctx['pricing_active'] = True
        return ctx


class BlogView(TemplateView):
    template_name = 'pages/blog.html'

    def get_context_data(self, **kwargs):
        ctx = super(BlogView, self).get_context_data(**kwargs)
        ctx['blog_active'] = True
        return ctx


class PodcastView(TemplateView):
    template_name = 'pages/podcast.html'

    def get_context_data(self, **kwargs):
        ctx = super(PodcastView, self).get_context_data(**kwargs)
        ctx['podcast_active'] = True
        return ctx


class ContactView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        ctx = super(ContactView, self).get_context_data(**kwargs)
        ctx['contact_active'] = True
        return ctx


class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        ctx = super(AboutView, self).get_context_data(**kwargs)
        ctx['about_active'] = True
        return ctx


class FAQView(TemplateView):
    template_name = 'pages/faq.html'

    def get_context_data(self, **kwargs):
        ctx = super(FAQView, self).get_context_data(**kwargs)
        return ctx


class PolicyView(TemplateView):
    template_name = 'pages/policy.html'

    def get_context_data(self, **kwargs):
        ctx = super(PolicyView, self).get_context_data(**kwargs)
        return ctx


class CancelPolicyView(TemplateView):
    template_name = 'pages/cancel_policy.html'

    def get_context_data(self, **kwargs):
        ctx = super(CancelPolicyView, self).get_context_data(**kwargs)
        return ctx


class TermsView(TemplateView):
    template_name = 'pages/terms.html'

    def get_context_data(self, **kwargs):
        ctx = super(TermsView, self).get_context_data(**kwargs)
        return ctx