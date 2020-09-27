from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'inicio.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        return ctx