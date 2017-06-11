from django.views.generic.base import TemplateView

import random
import string

class HomePageView(TemplateView):
    template_name = 'invento/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['name'] = ''.join(random.sample(string.ascii_lowercase, 6))
        return context
